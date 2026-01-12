import pandas as pd
import numpy as np
import os
from typing import Literal # Used for type hinting data_mode

def assign_xyz_groups(
    df: pd.DataFrame, 
    data_mode: Literal["dense", "sparse"] = "dense"
) -> pd.DataFrame:
    """
    Add 'XYZ', 'CV', and threshold columns to the original DataFrame.

    This function automatically determines X/Y thresholds based on the 33rd/66th
    percentiles of the Coefficient of Variation (CV) for all *eligible* SKUs.

    NEW PARAMETER:
    - data_mode (str):
        - "dense" (default): Replicates Excel behavior. Calculates mean/std
          across the *entire* period range for *all* SKUs. Missing periods
          for a SKU are filled with 0.0 before calculating stats.
        - "sparse": Calculates mean/std *only* using the periods provided
          for each SKU in the input data.

    Rules:
    - Input DataFrame MUST have columns: ['SKU', 'Period', 'Value'].
    - Aggregation at (SKU, Period) is always SUM.
    - SKUs with < 2 aggregated periods => XYZ = "" (Only applies in "sparse" mode)
    - SKUs with mean == 0 => cv = 0 and XYZ = "".
    - ... (rest of classification logic) ...
    """
    
    # --- 0. Validate new parameter ---
    if data_mode not in ["dense", "sparse"]:
        raise ValueError(f"data_mode must be 'dense' or 'sparse', not '{data_mode}'")
        
    # --- 1. Validate required columns ---
    required = {"SKU", "Period", "Value"}
    if not required.issubset(df.columns):
        missing = required - set(df.columns)
        raise ValueError(f"Missing required column(s): {missing}")

    # Work on a copy to avoid mutating caller's DataFrame
    df_out = df.copy()

    # --- 2. Ensure Value is numeric or convertible ---
    if not pd.api.types.is_numeric_dtype(df_out["Value"]):
        coerced = pd.to_numeric(df_out["Value"], errors="coerce")
        if coerced.isna().all():
            raise TypeError("'Value' column must be numeric or convertible to numeric.")
        df_out["Value"] = coerced.fillna(0.0)
    else:
        df_out["Value"] = df_out["Value"].fillna(0.0)

    # --- 3. Aggregate (SKU, Period) by SUM ---
    # This initial aggregation is always needed to ensure one value per SKU/Period
    period_sum = (
        df_out.groupby(["SKU", "Period"], as_index=False)["Value"]
        .sum()
    )

    # --- 3b. (NEW) Densify data if required ---
    # This block creates the DataFrame used for calculating stats
    
    if data_mode == "dense":
        # 1. Get all unique SKUs and Periods from the *original* data
        all_skus = df_out['SKU'].unique()
        all_periods = df_out['Period'].unique()

        # 2. Create a "scaffold" (Cartesian product) of all possible combinations
        df_scaffold = pd.MultiIndex.from_product(
            [all_skus, all_periods], 
            names=['SKU', 'Period']
        ).to_frame(index=False)

        # 3. Merge the aggregated data (period_sum) onto the scaffold
        # This creates a "dense" DataFrame
        df_dense = pd.merge(
            df_scaffold,
            period_sum,
            on=["SKU", "Period"],
            how="left"
        )

        # 4. Fill missing values (where no sales occurred) with 0.0
        df_dense["Value"] = df_dense["Value"].fillna(0.0)
        
        # 5. This dense DataFrame is now the input for stats calculation
        stats_input_df = df_dense
        
    else: # data_mode == "sparse"
        # Use the original sparse aggregation
        stats_input_df = period_sum


    # --- 4. Compute per-SKU statistics across aggregated periods ---
    # MODIFIED: Uses 'stats_input_df' which is either dense or sparse
    sku_stats = (
        stats_input_df.groupby("SKU", as_index=False)["Value"]
        .agg(n_periods="count", mean_value="mean", std_value="std")
    )
    # Note: In "dense" mode, 'n_periods' will be the total # of periods
    # for all SKUs. In "sparse" mode, it's the count of non-zero periods.
    # The classification logic handles this correctly.

    # Fill std=NaN with 0.0 for single-period SKUs (applies to sparse mode)
    sku_stats["std_value"] = sku_stats["std_value"].fillna(0.0)

    # --- 5. Compute CV (Vectorized) ---
    # (Unchanged)
    sku_stats['cv'] = np.where(
        sku_stats['mean_value'] == 0,
        0.0,  # Set CV to 0 if mean is 0
        sku_stats['std_value'] / np.abs(sku_stats['mean_value'])
    )
    
    # Handle potential inf/-inf results
    sku_stats['cv'] = sku_stats['cv'].replace([np.inf, -np.inf], np.nan)


    # --- 6. Determine Dynamic Thresholds ---
    # (Unchanged)
    MIN_PERIODS = 2 # This rule now only has a real effect in "sparse" mode

    is_eligible = (
        (sku_stats['n_periods'] >= MIN_PERIODS) &
        (sku_stats['mean_value'] != 0)
    )
    
    eligible_cvs = sku_stats.loc[is_eligible, 'cv'].dropna()

    if eligible_cvs.empty:
        x_threshold = 0.0
        y_threshold = 0.0
    else:
        quantiles = eligible_cvs.quantile([0.33, 0.66])
        # Automatic version
        x_threshold = quantiles[0.33]
        y_threshold = quantiles[0.66]
        # Manual version 
        # x_threshold = 0.5
        # y_threshold = 1

        if pd.isna(x_threshold) or pd.isna(y_threshold):
            x_threshold = 0.0
            y_threshold = 0.0

    # --- 7. Classify into X/Y/Z or blank "" (Vectorized) ---
    # (Unchanged)
    # The (n_periods < MIN_PERIODS) rule works correctly:
    # - In "dense" mode, it's always False (as n_periods = total periods)
    # - In "sparse" mode, it works as originally intended
    conditions = [
        (sku_stats['n_periods'] < MIN_PERIODS),
        (sku_stats['mean_value'] == 0),
        (sku_stats['cv'].isna()),
        (sku_stats['cv'] <= x_threshold), # "X"
        (sku_stats['cv'] <= y_threshold)  # "Y"
    ]
    
    choices = ["", "", "", "X", "Y"]
    default_choice = "Z"

    sku_stats['XYZ'] = np.select(conditions, choices, default=default_choice)

    # --- 8. Merge SKU-level labels back into the original DataFrame ---
    # (Unchanged)
    # We merge back onto the *original* df_out, not the dense one
    cols_to_merge = sku_stats[["SKU", "XYZ", "cv"]].rename(
        columns={"cv": "CV"}
    )

    merged = pd.merge(
        df_out,
        cols_to_merge,
        on="SKU",
        how="left",
        validate="m:1"  # many original rows to one sku_stats row
    )

    merged["XYZ"] = merged["XYZ"].fillna("")
    
    # --- 8b. Add threshold columns for debugging ---
    # (Unchanged)
    merged['x_threshold_33'] = x_threshold
    merged['y_threshold_66'] = y_threshold
    
    # --- 9. Final validation: ensure only allowed values present ---
    # (Unchanged)
    allowed = {"", "X", "Y", "Z"}
    unique_vals = set(merged["XYZ"].unique())
    disallowed = unique_vals - allowed
    if disallowed:
        raise RuntimeError(f"Unexpected XYZ values found: {disallowed}")

    # --- 10. Final column ordering ---
    # (Unchanged)
    new_cols = ["XYZ", "CV", "x_threshold_33", "y_threshold_66"]
    
    original_cols_to_keep = [
        c for c in df.columns if c not in new_cols
    ]
    
    final_cols = original_cols_to_keep + new_cols
    final = merged[final_cols]

    return final


def assign_xyz_groups_wide(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates XYZ classification and returns a SKU-level aggregated pivot table.

    REFACTORED: This function now calculates the 'CV' and 'XYZ' columns
    using "dense" data logic. It fills in 0.0 for all missing periods for
    all SKUs *before* calculating the mean, std, and CV. This matches
    Excel's behavior of calculating over a fixed range.
    
    1.  Calculates CV for all SKUs (Dense Method).
    2.  Calculates dynamic 33rd/66th percentile thresholds.
    3.  Applies 0.5/1.0 defaults if dynamic thresholds are 0.
    4.  Assigns 'XYZ' classification.

    OUTPUT:
    - PRINTS the final thresholds used for classification.
    - RETURNS a new DataFrame aggregated at the SKU level.
    
    DataFrame Format:
    - Index: None (standard 0...n)
    - Columns:
      - 'SKU'
      - [Period_1 (oldest)], [Period_2], ... [Period_N (newest)]
      - 'XYZ' (classification)
      - 'CV' (Coefficient of Variation, as the last column)
    """
    
    # --- 1. Validate required columns ---
    required = {"SKU", "Period", "Value"}
    if not required.issubset(df.columns):
        missing = required - set(df.columns)
        raise ValueError(f"Missing required column(s): {missing}")

    # Work on a copy to avoid mutating caller's DataFrame
    df_out = df.copy()

    # --- 2. Ensure Value is numeric or convertible ---
    if not pd.api.types.is_numeric_dtype(df_out["Value"]):
        coerced = pd.to_numeric(df_out["Value"], errors="coerce")
        if coerced.isna().all():
            raise TypeError("'Value' column must be numeric or convertible to numeric.")
        df_out["Value"] = coerced.fillna(0.0)
    else:
        df_out["Value"] = df_out["Value"].fillna(0.0)

    # --- 3. Aggregate (SKU, Period) by SUM ---
    # This sparse aggregation is the source for the pivot table *and*
    # the merge onto the dense scaffold.
    period_sum = (
        df_out.groupby(["SKU", "Period"], as_index=False)["Value"]
        .sum()
    )

    # --- 3b. (NEW) Densify data for stats calculation ---
    # This block creates a dense DataFrame (all SKUs x all Periods)
    # to be used *only* for calculating the CV and XYZ stats.
    
    # 1. Get all unique SKUs and Periods
    all_skus = df_out['SKU'].unique()
    all_periods = df_out['Period'].unique()

    # 2. Create a "scaffold" (Cartesian product)
    df_scaffold = pd.MultiIndex.from_product(
        [all_skus, all_periods], 
        names=['SKU', 'Period']
    ).to_frame(index=False)

    # 3. Merge the actual sales data (period_sum) onto the scaffold
    df_dense_stats_source = pd.merge(
        df_scaffold,
        period_sum,
        on=["SKU", "Period"],
        how="left"
    )

    # 4. Fill missing values (where no sales occurred) with 0.0
    df_dense_stats_source["Value"] = df_dense_stats_source["Value"].fillna(0.0)


    # --- 4. Compute per-SKU statistics across aggregated periods ---
    # MODIFIED: This now uses the 'df_dense_stats_source'
    sku_stats = (
        df_dense_stats_source.groupby("SKU", as_index=False)["Value"]
        .agg(n_periods="count", mean_value="mean", std_value="std")
    )

    # Fill std=NaN with 0.0 (e.g., if only 1 period exists)
    sku_stats["std_value"] = sku_stats["std_value"].fillna(0.0)

    # --- 5. Compute CV (Vectorized) ---
    # This CV is now calculated on the DENSE data
    sku_stats['cv'] = np.where(
        sku_stats['mean_value'] == 0,
        0.0,  # Set CV to 0 if mean is 0
        sku_stats['std_value'] / np.abs(sku_stats['mean_value'])
    )
    
    # Handle potential inf/-inf results
    sku_stats['cv'] = sku_stats['cv'].replace([np.inf, -np.inf], np.nan)


    # --- 6. Determine Dynamic Thresholds ---
    MIN_PERIODS = 2
    # Note: In dense mode, 'n_periods' will be the total count of periods
    # for all SKUs, so (n_periods >= MIN_PERIODS) will always be True.
    is_eligible = (
        (sku_stats['n_periods'] >= MIN_PERIODS) &
        (sku_stats['mean_value'] != 0)
    )
    eligible_cvs = sku_stats.loc[is_eligible, 'cv'].dropna()

    if eligible_cvs.empty:
        # Fallback 1: No eligible SKUs.
        x_threshold = 0.0
        y_threshold = 0.0
    else:
        # Calculate 33rd and 66th quantiles
        quantiles = eligible_cvs.quantile([0.33, 0.66])
        # Automatic version
        x_threshold = quantiles[0.33]
        y_threshold = quantiles[0.66]
        # Manual version 
        # x_threshold = 0.5
        # y_threshold = 1

        # Fallback 2: Handle edge cases
        if pd.isna(x_threshold) or pd.isna(y_threshold):
            x_threshold = 0.0
            y_threshold = 0.0

    # Fallback 3: Override if thresholds are 0
    # *** BUG FIX ***: Corrected to apply 0.5/1.0, not just reassign the same value
    if x_threshold == 0.0 or y_threshold == 0.0:
        x_threshold = 0.5
        y_threshold = 1.0

    # --- 7. Print Final Thresholds ---
    print("--- XYZ Classification Thresholds (Dense) ---")
    print(f"33rd Percentile (x_threshold): {x_threshold}")
    print(f"66th Percentile (y_threshold): {y_threshold}")
    print("---------------------------------------------")


    # --- 8. Classify into X/Y/Z or blank "" (Vectorized) ---
    # This classification is now based on the DENSE stats
    conditions = [
        (sku_stats['n_periods'] < MIN_PERIODS), # Will be False in dense mode
        (sku_stats['mean_value'] == 0),
        (sku_stats['cv'].isna()),
        (sku_stats['cv'] <= x_threshold), # "X"
        (sku_stats['cv'] <= y_threshold)  # "Y"
    ]
    choices = ["", "", "", "X", "Y"]
    default_choice = "Z"
    sku_stats['XYZ'] = np.select(conditions, choices, default=default_choice)

    # --- 9. Create Period Pivot Table ---
    # This step is UNCHANGED. It correctly uses the *original* 'period_sum'
    # to build the pivot, which is what the user wants to see.
    period_pivot = pd.pivot_table(
        period_sum,
        values='Value',
        index='SKU',
        columns='Period',
        aggfunc='sum',
        fill_value=0.0  # Fill missing periods for a SKU with 0
    )

    # --- 10. Sort Pivot Columns Chronologically ---
    period_pivot = period_pivot.sort_index(axis=1)
    
    # Get the sorted list of period columns for final ordering
    period_cols = list(period_pivot.columns)

    # --- 11. Merge Stats into Pivot Table ---
    # This step is UNCHANGED, but 'sku_stats' now contains the
    # CV and XYZ values calculated from the DENSE data.
    stats_to_merge = sku_stats[['SKU', 'XYZ', 'cv']].rename(
        columns={'cv': 'CV'}
    )

    final_df = pd.merge(
        period_pivot.reset_index(),
        stats_to_merge,
        on='SKU',
        how='left'
    )

    # --- 12. Final Column Ordering & Cleanup ---
    final_cols = ['SKU'] + period_cols + ['XYZ', 'CV']
    final_df = final_df[final_cols]
    
    final_df['XYZ'] = final_df['XYZ'].fillna("")

    return final_df


# Saving in the same folder as the Python (py or ipynb) file using one of two popular Excel libraries
def save_file(data: pd.DataFrame, name: str) -> None:
    """
    Saves a DataFrame to an Excel file using the preferred engine.
    Falls back to openpyxl if xlsxwriter is unavailable.
    """
    dump_file_name = f"{name}.xlsx"
    data_dump = os.path.join(os.getcwd(), dump_file_name)

    try:
        # Try xlsxwriter first (faster, supports formatting)
        writer = pd.ExcelWriter(data_dump, engine="xlsxwriter")
    except ModuleNotFoundError:
        print("⚠️  xlsxwriter not found. Falling back to openpyxl.")
        writer = pd.ExcelWriter(data_dump, engine="openpyxl")

    # Write to Excel
    data.to_excel(writer, sheet_name=name, index=False)

    # Save and close the writer properly
    writer.close()
    print(f"✅ Data successfully saved as: {data_dump}")


#Execution:
value_field = 'Sales'
# File paths for input CSV files
file_path = "C:\\Python repositories\\Education project\\src\\data\\input\\" + value_field + ".csv"

# Load input data
xyz_table = pd.read_csv(file_path, sep=';')

# Replace comma with dot and convert to float
xyz_table[value_field] = xyz_table[value_field].str.replace(',', '.').astype(float)

# Change Date column to datetime format
# REFRACTORED: Added dayfirst=True to correctly parse DD.MM.YYYY format
xyz_table['Date'] = pd.to_datetime(xyz_table['Date'], dayfirst=True)

# Create a string Period column from Date
# New column
xyz_table['Period'] = xyz_table['Date']
# Change format
xyz_table['Period'] = pd.to_datetime(xyz_table['Date']).dt.strftime('%Y-%m')
# Delete old column
del xyz_table['Date']

# Renaming column to a default input column for XYZ analysis 'Value'
xyz_table.rename(columns={
                value_field: 'Value',
},inplace=True)

# Choose columns in a specific order as copy
required_cols = ['SKU', 'Period', 'Value']
xyz_input = xyz_table[required_cols].copy()

# Aggregate values by on SKU, Period level
aggregation_cols = ['SKU','Period']
xyz_input = xyz_input.groupby(aggregation_cols, as_index=False).agg(
{'Value':'sum'})

# XYZ classification operation
df_result = assign_xyz_groups(xyz_input)
df_wide_result = assign_xyz_groups_wide(xyz_input)

# Save output file
save_file(df_result, "xyz_"+value_field)
save_file(df_wide_result, "xyz_wide_"+value_field)
