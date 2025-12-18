### Mindset
**Make as many mistakes as you can in a shortest amount of time so that you can learn from them. Mistakes and errors are your friend and you can be proud of them.**
### Excel Shortcuts Hotkeys:
|🧩 **Action**|⌨️ **Windows Shortcut**|🍎 **Mac Shortcut**|📝 **Notes**|
|:--|:--|:--|:--|
|**Array formula**|`Ctrl + Shift + Enter`|`⌃ + Shift + Return`|Confirms array formulas (older Excel versions).|
|**Block cell selection with dollar symbols** _(absolute references)_|`F4`|`⌘ + T` _(or `Fn + F4` on laptops)_|Cycles `$A$1`, `A$1`, `$A1`, etc.|
|**Create filter**|`Ctrl + Shift + L`|`⌃ + Shift + L` _(or `⌘ + Shift + F`)_|Adds/removes column filters.|
|**Create table (structured Table)**|`Ctrl + T`|`⌘ + T`|Converts range into a structured Excel Table.|
|**Create _list-type_ table (legacy)**|`Ctrl + L`|`⌃ + L`|Creates a “List Object,” Excel’s older table form.|
|**Drop-down list of existing values**|_(N/A)_|`⌥ + ↓`|Shows existing entries from the column.|
|**Edit cell**|`F2`|`⌃ + U`|Opens cell for editing.|
|**Find and Replace**|`Ctrl + H`|`⌘ + Shift + H` _(or `⌘ + F` to find only)_|Opens the Find/Replace dialog.|
|**Go until the end of values**|`Shift + (Arrow)`|`Shift + (Arrow)`|Extends selection to data end.|
|**Go to section (jump to end)**|`Ctrl + (Arrow)`|`⌘ + (Arrow)`|Moves to edge of data region.|
|**Next sheet**|`Ctrl + PageDown`|`⌘ + Option + →` _(or `Fn + ⌃ + ↓`)_|Moves to next worksheet tab.|
|**Previous sheet**|`Ctrl + PageUp`|`⌘ + Option + ←` _(or `Fn + ⌃ + ↑`)_|Moves to previous worksheet tab.|
|**Repeat last action**|`Ctrl + Y`|`⌘ + Y` _(or `⌘ + Shift + Z`)_|Repeats the last command or action.|
|**Select all**|`Ctrl + A`|`⌘ + A`|Selects all cells in the current data region.|
|**Select all until the end of values**|`Ctrl + Shift + (Arrow)`|`⌘ + Shift + (Arrow)`|Selects to the end of contiguous data.|
|**Select column**|`Ctrl + Space`|`⌃ + Space`|Selects the entire column of the active cell.|
|**Select section (jump selection)**|`Ctrl + Shift + (Arrow)`|`⌘ + Shift + (Arrow)`|Expands selection to data edge.|
|**Select object**|`Ctrl + Shift + Space`|`⌃ + Shift + Space`|Selects all objects (charts, shapes, etc.)|
|**Select row**|`Shift + Space`|`Shift + Space`|Selects the entire row.|
|**Spread formula or text to multiple lines**|`Alt + Enter`|`⌃ + Option + Return`|Inserts a line break within a cell or formula.|
|**Two decimal places + thousand separator**|`Ctrl + Shift + !`|`⌘ + Shift + !`|Applies number format with commas and two decimals.|
|**Undo last action**|`Ctrl + Z`|`⌘ + Z`|Reverts last action.|
### Python Jupyter Lab Notebook Shortcuts Hotkeys
- Change the order of sections: **Drag and Drop**
- Comment or Uncomment section: **Ctrl + /**
- Hide files section: **Ctrl + B**
- Indentation: **Tab**
- Markdown (comment) section: **M**
- New section above: **A**
- New section below: **B**
- Remove section: **X**
- Reverse indentation: **Shift + Tab**
- Run section: **Shift + Enter**
### Definitions
- **Coefficient of Variation (CV)** - a dispersion measure. A ratio of standard variation and mean.
Coefficient of variation:
```
Coefficient of variation:
CV = σ / μ  
```
Sample coefficient of variation:
```
Sample coefficient of variation: 
CV = s / x̄
```
- **CSV** - Comma-Separated Values. The most common text data format.
- **Decile** - a ten group quantile. Values that divide a data set, ordered from smallest to largest, into ten equal parts, representing 10% of the data points in each segment. 
- **Distribution** - describes the possible values of a random variable and how often each value occurs within a dataset. It provides a framework for understanding the frequency, likelihood, and spread of different outcomes.
- **Histogram** - a visual representation of the distribution of quantitative data. A diagram consisting of rectangles whose area is proportional to the frequency of a variable and whose width is equal to the class interval.
- **Long and wide data format** - Long (narrow or stacked or vertical) format means each row is an observation, while wide (horizontal or unstacked) format spreads variables across columns.
- **Median** - a second of four group quantile or a second quartile. Values that divide a data set, ordered from smallest to largest, into two equal parts, representing 50% of the data points in each segment. 
- **Melting** - transposes the data from horizontal to vertical format. Melt function in Python. Transpose tool in Alteryx.
- **Quartile** - a four group quantile. Values that divide a data set, ordered from smallest to largest, into four equal parts, representing 25% of the data points in each segment. 
- **Quantile** - a point that divides a dataset into equal-sized subgroups, such that a certain percentage of the data falls below that point. Common quantiles have special names, such as quartiles (four groups), deciles (ten groups), and percentiles (100 groups). 
- **Percentile** - a hundred group quantile. Values that divide a data set, ordered from smallest to largest, into hundred equal parts, representing 1% of the data points in each segment. 
- **Pivoting** - transposes the data from vertical to horizontal format. Creates columns from rows. Pivot function in Python. Cross Tab tool in Alteryx.
- **Standard deviation** - a statistical measure of data spread around the mean, indicating how much individual data points vary from the average
Population standard deviation:
```
Population standard deviation:
σ = √( Σᵢ₌₁ᴺ (xᵢ − μ)² / N )
```
Sample standard deviation:
```
Sample standard deviation:
s = √( Σᵢ₌₁ⁿ (xᵢ − x̄)² / (n − 1) )
```
- **Variance** - a statistical measure of the _spread or dispersion_ of data points in a set relative to their mean (average).

Population variance: 
```
Population variance:
σ² = Σᵢ₌₁ᴺ (xᵢ − μ)² / N
```
Sample variance: 
```
Sample variance:
s² = Σᵢ₌₁ⁿ (xᵢ − x̄)² / (n − 1)
```
- **SKU** - Stock Keeping Unit. Alphanumeric symbol for a type of physical good a company uses. Basis for masterdata management.
### Techniques
- **Pivoting stock data (B column) from long to wide format by period (A column) per SKU (C column) multiplied by the price (in T column):**
``` excel
=SUMIFS('Stock history'!$B$2:$B$90000;'Stock history'!$C$2:$C$90000;$A2;'Stock history'!$A$2:$A$90000;B$1)*$T2
```
- **Nested IF function with two conditions with percentiles as thresholds:**
``` excel
=IF(U2<=2,16;"X";(IF(U2<=2,4;"Y";"Z")))
or 
=IF(V3<=PERCENTILE.INC($W$3:$W$3881;0,33);"X";(IF(V3<=PERCENTILE.INC($W$3:$W$3881;0,66);"Y";"Z")))
```
- **Period from Date field:**
``` excel
=IF(MONTH(B2)<10;YEAR(B2)&"-0"&MONTH(B2);YEAR(B2)&"-"&MONTH(B2))
or
=TEXT(B2;"yyyy-mm")
// polish version
=TEKST(B2;"rrrr-mm")
```
### Excel Functions
- **Adds values. You can add individual values, cell references or ranges or a mix of all three:**
``` excel
SUM(number1,[number2],...)
```
- **Find things in a table or a range by row. Value you want to look up must be in the first column of the range. The column number that contains the return value. Use last value as 0 for exact match:**
``` excel
VLOOKUP (lookup_value, table_array, col_index_num, [range_lookup])
```
- **Look in one column for a search term and return a result from the same row in another column, regardless of which side the return column is on:**
``` excel
XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found], [match_mode], [search_mode])
```
- **Searches for a specified item in a range of cells, and then returns the relative position of that item in the range:**
``` excel
MATCH(lookup_value, lookup_array, [match_type])
```
- **Returns a value or the reference to a value from within a table or range:**
``` excel
INDEX(array, row_num, [column_num])
```
- **Show a certain value when error like zero `0` or empty cell `""`**
``` excel
IFERROR(value, value_if_error)
```
- **INDEX with MATCH as improved VLOOKUP (it does what VLOOKUP and more like intersection). Find value from A2 in the column of A up to A200 and show value from the same row but from column B:**
``` excel
IFERROR(INDEX(Sheet1'!$B$2:$B$200;MATCH(A2;'Sheet1'!$A$2:$A$200;0));"")
```
- **Adds all of its arguments that meet multiple criteria. Sum many rows based on intersection of many criteria. Value 1 in column 1, value 2 in column 2 etc.:**
``` excel
SUMIFS(sum_range, criteria_range1, criteria1, [criteria_range2, criteria2], ...)
```
-  **Logical comparisons between a value and what you expect. IF statement can have two results. The first result is if your comparison is True, the second if your comparison is False:**
``` excel
IF(logical_test, value_if_true, [value_if_false])
```
- **Returns the k-th percentile of values in a range, where k is in the range 0 to 1, inclusive. This function is the new version (from 2010) of PERCENTILE function.**
``` excel
PERCENTILE.INC(array,k)
```
- **The TEXT function lets you change the way a number appears by applying formatting to it with format codes. It's useful in situations where you want to display numbers in a more readable format, or you want to combine numbers with text or symbols.**
``` excel
=TEXT(Value you want to format, "Format code you want to apply")
```
### Power BI functions
- **Returns the first expression that does not evaluate to BLANK. If all expressions evaluate to BLANK, BLANK is returned.:**
``` excel
COALESCE(<expression>, <expression>[, <expression>]…)
```
- **Returns a related value from another table. When the RELATED function performs a lookup, it examines all values in the specified table regardless of any filters that may have been applied.`RELATED(<Table>[Column])` fetches the _single value_ of `<Column>` from a table that is related to the current table via a model relationship. Conceptually it performs a lookup from the current row (row context) to the related table following the relationship path defined in the data model. It is designed to be used where a one-to-many relationship exists and you are on the many side (e.g., `Stock` many → `COGS` one).:**
``` excel
RELATED(<column>)
```
- **Returns the value for the row that meets all criteria specified by one or more search conditions. The value of `result_columnName` at the row where all pairs of `search_columnName` and `search_value` have an exact match. If there isn't a match that satisfies all the search values, BLANK or `alternateResult` (if specified) is returned. In other words, the function doesn't return a lookup value if only some of the criteria match. If multiple rows match the search values and the values in the `result_columnName` for these rows are identical, then that value is returned. However, if `result_columnName` returns different values, an error or `alternateResult` (if specified) is returned.:**

|Term|Definition|
|---|---|
|`result_columnName`|The name of an existing column that contains the value you want to return. It cannot be an expression.|
|`search_columnName`|The name of an existing column. It can be in the same table as result_columnName or in a related table. It cannot be an expression. Multiple pairs of search_columnName and search_value can be specified.|
|`search_value`|The value to search for in search_columnName. Multiple pairs of search_columnName and search_value can be specified.|
|`alternateResult`|(Optional) The value returned when the context for result_columnName has been filtered down to zero or more than one distinct value. If not specified, the function returns BLANK when result_columnName is filtered down to zero values or an error when there is more than one distinct value in the context for result_columnName.|
``` excel
LOOKUPVALUE (
    <result_columnName>,
    <search_columnName>,
    <search_value>
    [, <search2_columnName>, <search2_value>]…
    [, <alternateResult>]
)
```
- **Adds all the numbers in a column.:**
``` excel
SUM(<column>)
```
- **Evaluates an expression in a modified filter context.:**
``` excel
CALCULATE(<expression>[, <filter1> [, <filter2> [, …]]])
```
- **Returns a table that represents a subset of another table or expression.:**
``` excel
FILTER(<table>,<filter>)
```
- **Stores the result of an expression as a named variable, which can then be passed as an argument to other measure expressions. Once resultant values have been calculated for a variable expression, those values do not change, even if the variable is referenced in another expression.:**
``` excel
VAR <name> = <expression>
```
- **Returns the ranking of a number in a list of numbers for each row in the `table` argument.:**
``` excel
RANKX(<table>, <expression>[, <value>[, <order>[, <ties>]]])
```
- **Returns all the rows in a table, or all the values in a column, ignoring any filters that might have been applied. This function is useful for clearing filters and creating calculations on all the rows in a table.:**
``` excel
ALL( [<table> | <column>[, <column>[, <column>[,…]]]] )
```
- **Performs division and returns alternate result or BLANK() on division by 0.:**
``` excel
DIVIDE(<numerator>, <denominator> [,<alternateresult>])
```
- **Calculates the average (arithmetic mean) of a set of expressions evaluated over a table.:**
``` excel
AVERAGEX(<table>,<expression>)
```
- **Removes all context filters in the table except filters that have been applied to the specified columns.:**
``` excel
ALLEXCEPT(<table>,<column>[,<column>[,…]])
```
- **Applies the result of a table expression as filters to columns from an unrelated table.:**
``` excel
TREATAS(table_expression, <column>[, <column>[, <column>[,…]]]} )
```
- **When the input parameter is a column name, returns a one-column table that contains the distinct values from the specified column. Duplicate values are removed and only unique values are returned. A BLANK value can be added. When the input parameter is a table name, returns the rows from the specified table. Duplicate rows are preserved. A BLANK row can be added.:**
``` excel
VALUES(<TableNameOrColumnName>)
```
- **Returns the standard deviation of the entire population.:**
``` excel
STDEVX.P(<table>, <expression>)
```
- **Checks a condition, and returns one value when it's `TRUE`, otherwise it returns a second value.:**
``` excel
IF(<logical_test>, <value_if_true>[, <value_if_false>])
```
- **Evaluates an expression against a list of values and returns one of multiple possible result expressions. This function can be used to avoid having multiple nested IF statements.:**
``` excel
SWITCH(<expression>, <value>, <result>[, <value>, <result>]…[, <else>])
```
- **Converts a value to text according to the specified format.:**
``` excel
FORMAT(<value>, <format_string>[, <locale_name>])
```
### XYZ analysis in Excel
### Main formula

``` mermaid
flowchart TD
    A[Start] --> B{Is V2 <= 2,16?}
    B -- Yes --> X["Return 'X'"]
    B -- No --> C{Is V2 <= 2,4?}
    C -- Yes --> Y["Return 'Y'"]
    C -- No --> Z["Return 'Z'"]
    X --> End[End]
    Y --> End
    Z --> End
```
``` excel
=IF(V2<=2,16;"X";IF(V2<=2,4;"Y";"Z"))
```
### Execution steps
**XYZ groups definition:**
- X - stable SKUs
- Y - less stable SKUs
- Z - not stable SKUs

**Opening data:**
Double-click it or use File > Open in Excel. If Unicode characters don't display correctly, import it via Excel's Data tab > Get Data > From Text/CSV.

**XYZ analysis in Excel:**
1. "Stock history" table usually as ERP data dump in long format. Stock quantity at the end of the calendar month.
2. Copy all SKUs and paste to "Table" sheet as values and remove duplicates. 
```
Excel -> Data -> Remove Duplicates
```
3. Copy all periods from "Stock history" and remove duplicates. Paste them transposed as columns in "Table" sheet. 
4. Use SUMIFS function to populate stock quantity:
``` excel
=SUMIFS('Stock history'!$B$2:$B$90000;'Stock history'!$C$2:$C$90000;$A2;'Stock history'!$A$2:$A$90000;B$1)
```
3. For XYZ analysis calculate coefficient of variation as new column. As the data source use quantity for every period per SKU. Use standard deviation of the population if we have whole history of stock or sample standard deviation if we use a subset of history (the difference is not important for the business). Population answers the question of: How much did this SKU's sales _actually_ vary during these 18 months? Sample is the standard for _inferential statistics_. It provides an **unbiased estimator** of the true, underlying population variance.:
``` excel
IF(AVERAGE(C3:T3)=0;0;STDEV.P(C3:T3)/AVERAGE(C3:T3))
or 
IFERROR(STDEV.P(C3:T3)/AVERAGE(C3:T3);0)
```
6. Select CV column and create a histogram chart in "Charts" sheet to find the best boundary conditions for XYZ groups.
7. For XYZ analysis calculate XYZ groups as new column with thresholds based on the manual analysis of the histogram of the population of variability measure (CV) or based on X being the 33rd percentile and Y being between 33rd and 66th percentile of variability measure (CV) population:
``` excel
IF(U2<=2,16;"X";(IF(U2<=2,4;"Y";"Z")))
or 
IF(V3<=PERCENTILE.INC($W$3:$W$3881;0,33);"X";(IF(V3<=PERCENTILE.INC($W$3:$W$3881;0,66);"Y";"Z")))
```
8. Use conditional formatting for XYZ classification cells with X as Green, Y as Yellow and Z as Red or vice versa. 
```
Excel -> Home -> Conditional Formatting -> Highlight Cell Rules -> Text that Contains
```
### XYZ analysis in Power BI
#### Main formula
**XYZ analysis assuming that there are fixed thresholds separating X and Y and Z groups:**
``` excel
XYZ = 
VAR AllPeriods =
    ALL('Sales'[Period]) 
    // Ensures we iterate over all available periods in the model, not just those with activity for the SKU

// --- Calculate Average Sales across ALL periods including zero periods ---
VAR AvgSales =
    AVERAGEX(
        AllPeriods,
        COALESCE(
            CALCULATE(
                SUM('Sales'[Sales]),
                ALLEXCEPT('Sales', 'Sales'[SKU]),  // keep SKU fixed
                TREATAS(VALUES('Sales'[Period]), 'Sales'[Period]) // ensure period context
            ),
            0
        )
    )

// --- Calculate Std Dev across ALL periods including zeros ---
VAR StdDevSales =
    STDEVX.P(
        AllPeriods,
        COALESCE(
            CALCULATE(
                SUM('Sales'[Sales]),
                ALLEXCEPT('Sales', 'Sales'[SKU]),
                TREATAS(VALUES('Sales'[Period]), 'Sales'[Period])
            ),
            0
        )
    )

// --- Coefficient of Variation ---
VAR CoV = DIVIDE(StdDevSales, AvgSales, 0)

// --- Classification ---
RETURN
    SWITCH(
        TRUE(),
        CoV <= 2.16, "X",
        CoV <= 2.4, "Y",
        "Z"
    )

/*
--- Explanation ---
- ALL('Sales'[Period]) iterates over all known periods globally
- COALESCE wraps the measure to replace blanks with 0 for missing periods
- ALLEXCEPT('Sales', 'Sales'[SKU]) locks calculation on current SKU
- TREATAS ensures correct period context during iteration
- Avg and StdDev now reflect missing periods accurately
*/
```
**More resilient version where fixed thresholds of `2.16` and `2.4` have been replaced with 33rd and 66th percentiles of Coefficient of Variation values:**
``` excel
XYZ =
VAR AllPeriods =
    ALL('Sales'[Period])

// --- Calculate Average Sales across ALL periods including zero periods ---
VAR AvgSales =
    AVERAGEX(
        AllPeriods,
        COALESCE(
            CALCULATE(
                SUM('Sales'[Sales]),
                ALLEXCEPT('Sales', 'Sales'[SKU]),
                TREATAS(VALUES('Sales'[Period]), 'Sales'[Period])
            ),
            0
        )
    )

// --- Calculate Std Dev across ALL periods including zeros ---
VAR StdDevSales =
    STDEVX.P(
        AllPeriods,
        COALESCE(
            CALCULATE(
                SUM('Sales'[Sales]),
                ALLEXCEPT('Sales', 'Sales'[SKU]),
                TREATAS(VALUES('Sales'[Period]), 'Sales'[Period])
            ),
            0
        )
    )

// --- Coefficient of Variation ---
VAR CoV =
    DIVIDE(StdDevSales, AvgSales, 0)

// --- Percentile thresholds across all SKUs ---
VAR P33 =
    PERCENTILEX.INC(
        ALL('Sales'[SKU]),
        CoV,
        0.33
    )

VAR P66 =
    PERCENTILEX.INC(
        ALL('Sales'[SKU]),
        CoV,
        0.66
    )

// --- Classification ---
RETURN
    SWITCH(
        TRUE(),
        CoV <= P33, "X",
        CoV <= P66, "Y",
        "Z"
    )
```
### XYZ analysis in Python
**Basic code:**
``` python
# Coeficient of variation per row for all integer columns in a DataFrame
# Selecting integer only columns
int_cols = list(df.select_dtypes(include=['int']))
# Calculating coefficient of variation (CV) for each row across all integer columns
# CV = (standard deviation / mean) * 100 (as percentage)
df['cv'] = np.where(
    df[int_cols].mean(axis=1) != 0,
    (df[int_cols].std(axis=1) / df[int_cols].mean(axis=1).abs()) * 100,  # Use abs(mean) to handle negative means if applicable
    np.nan  # Set to NaN if mean is zero
)
# New XYZ column with 3 rules
df['XYZ'] = np.where((df['cv']<=4.32),'Z','')
df['XYZ'] = np.where((df['cv']<=2.40),'Y',df['XYZ'])
df['XYZ'] = np.where((df['cv']<=2.16),'X',df['XYZ'])
```
#### Automated XYZ analysis in Python
Transforming data for the specific input format:
1. Loading Pandas library:
``` python
import pandas as pd
```
2. Loading stock data. XYZ analysis (the variability analysis) of sales data or historical stock data done on quantities and values will give the same result. Therefore we don't need to multiply the quantities by prices and we can load only stock quantity data:
``` python
# Stock data loading
file_path = "C:\\Python repositories\\Education project\\src\\data\\input\\Stock.xlsx"
stock = pd.read_excel(file_path)
```
3. If the input data is loaded as dates we need to change them to Period format so that we can aggregate by Period later:
``` python
# Create a string Period column from Date
# New column
stock['Period'] = stock['Date']
# Change format
stock['Period'] = pd.to_datetime(stock['Date']).dt.strftime('%Y-%m')
# Delete old column
del stock['Date']
```
4. XYZ function should have a default naming convention for input. If our input columns have different names we should adjust them to default. For example if our XYZ function requires input column name "Value" and our numerical column is named "Stock":
``` python
# Renaming column to a default input column for XYZ analysis 'Value'
stock.rename(columns={
                'Stock': 'Value',
},inplace=True)
```
5. Create XYZ analysis function with output in long format.
   This function will split the distribution of CV values into three equal parts and assign X to the most stable Y to the middle group and Z to the least stable. If we want to assign groups manually we can edit the following part of the function and comment out two lines after "Automatic version" and uncomment two lines after "Manual version":
``` python
# Calculate 33rd and 66th quantiles
quantiles = eligible_cvs.quantile([0.33, 0.66])
# Automatic version
x_threshold = quantiles[0.33]
y_threshold = quantiles[0.66]
# Manual version 
# x_threshold = 0.5
# y_threshold = 1
```
   The function on default will fill all the missing periods with quantity of 0 (dense version). 
   For example for stock data if we have stock at the end of January and March but at the end of February there was no stock there could be no record for February. However we should take into account February as 0 amount of stock to analyze full spectrum of stock changes from Period to Period:
``` python
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
```
6. Execute function for XYZ classification operation:
``` python
# XYZ classification operation
df_result = assign_xyz_groups(stock)
```
7. Create save to excel function:
``` python
import os

# Saving in the same folder as the Python (py or ipynb) file using one of two popular Excel libraries
def save_local_file(data: pd.DataFrame, name: str) -> None:
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
```
8. Save output file:
``` python
# Save output file
save_local_file(df_result, "xyz")
```
