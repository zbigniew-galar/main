import pandas as pd
import numpy as np


class analysis_func:


    # ABC Classification function
    def assign_abc_groups(df: pd.DataFrame, a_threshold: float = 0.80, b_threshold: float = 0.95) -> pd.DataFrame:
        """
        Assigns ABC classification groups to SKUs per Period based on cumulative value contribution.

        Enhancements:
        -------------
        - Handles cases where total period value is 0 by assigning all SKUs in that period to group 'C'.

        Parameters
        ----------
        df : pd.DataFrame
            Input DataFrame with columns ['SKU', 'Period', 'Value'].
        a_threshold : float, optional
            Cumulative contribution cutoff for class A (default=0.80).
        b_threshold : float, optional
            Cumulative contribution cutoff for class B (default=0.95).

        Returns
        -------
        pd.DataFrame
            DataFrame with columns ['SKU', 'Period', 'Value', 'ABC_Group'].

        Raises
        ------
        ValueError
            If required columns are missing.
        TypeError
            If 'Value' is not numeric.
        """

        # === 1. Input validation ===
        required_columns = {'SKU', 'Period', 'Value'}
        if not required_columns.issubset(df.columns):
            missing = required_columns - set(df.columns)
            raise ValueError(f"Missing required columns: {missing}")

        if not pd.api.types.is_numeric_dtype(df['Value']):
            raise TypeError("'Value' column must be numeric (float or int).")

        # Fill missing values in Value column
        df = df.copy()
        df['Value'] = df['Value'].fillna(0.0)

        # === 2. Aggregate total values per SKU/Period ===
        agg_df = (
            df.groupby(['Period', 'SKU'], as_index=False)['Value']
            .sum()
        )

        # === 3. Sort, rank and compute cumulative metrics ===
        agg_df = agg_df.sort_values(['Period', 'Value'], ascending=[True, False])

        # Compute total value per Period
        agg_df['Total_Period_Value'] = agg_df.groupby('Period')['Value'].transform('sum')

        # Compute cumulative value per Period
        agg_df['Cumulative_Value'] = agg_df.groupby('Period')['Value'].cumsum()

        # Handle division safely: if total = 0, set cumulative percent = 1 (forcing C group)
        agg_df['Cumulative_Percent'] = np.where(
            agg_df['Total_Period_Value'] == 0,
            1.0,
            agg_df['Cumulative_Value'] / agg_df['Total_Period_Value']
        )

        # === 4. ABC Group assignment ===
        def classify_abc(cum_pct: float, total_val: float) -> str:
            """
            Determine ABC class:
            - If total value = 0  → assign 'C'
            - Else apply thresholds normally.
            """
            if total_val == 0:
                return 'C'
            if cum_pct <= a_threshold:
                return 'A'
            elif cum_pct <= b_threshold:
                return 'B'
            else:
                return 'C'

        # Apply classification row-wise
        agg_df['ABC_Group'] = agg_df.apply(
            lambda x: classify_abc(x['Cumulative_Percent'], x['Total_Period_Value']),
            axis=1
        )

        # === 5. Merge results back into original DataFrame ===
        result_df = pd.merge(
            df,
            agg_df[['Period', 'SKU', 'ABC_Group']],
            on=['Period', 'SKU'],
            how='left'
        )

        # === 6. Validation ===
        if result_df['ABC_Group'].isna().any():
            raise RuntimeError("ABC group assignment failed for some rows.")

        return result_df