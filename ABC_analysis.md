### Mindset
**Make as many mistakes as you can in a shortest amount of time so that you can learn from them. Mistakes and errors are your friend and you can be proud of them.**
### Shortcuts Hotkeys:
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
### Definitions
**Pareto analysis definition:**
Pareto analysis sets priorities for action based on the assumption that roughly 80 percent of problems typically result from 20 percent of the possible causes. Thus, not all possible causes of problems are equally important. Pareto analysis identifies the most critical (most frequent) causes of problems so that improvement efforts can be focused where the investment of time, effort, and money will yield the largest return.
**Pareto analysis consists of a four-step procedure:**
1. Identify categories about which to collect information. For example, specify categories that describe possible causes or types of defects. Such categories could come from a cause-and-effect analysis.
2. Gather the data and calculate the frequency of observations in each category for an appropriate time period. A check sheet could be used to guide data collection.
3. Sort the categories in descending order based on their percentages.
4. Present the data graphically

**Source:** Swink, M., Melnyk, S. and Hartley, J.L. (2024) _Managing Operations Across the Supply Chain_. New York: McGraw Hill. p. 212.

- **Cardinality** -  refers to the uniqueness of values within a relationship in a data model and describes how many occurrences of one entity connect to occurrences of another entity.
- **CSV** - Comma-Separated Values. The most common text data format.
- **Long and wide data format** - Long (narrow or stacked or vertical) format means each row is an observation, while wide (horizontal or unstacked) format spreads variables across columns.
- **Pivoting** - transposes the data from vertical to horizontal format. Creates columns from rows. Pivot function in Python. Cross Tab tool in Alteryx.
- **SKU** - Stock Keeping Unit. Alphanumeric symbol for a type of physical good a company uses. Basis for masterdata management.
### Techniques
- **Connecting price data from B column of `COGS` table to the stock table based on the SKUs from C column that can be found in A column of `COGS` table:**
``` excel
=IFERROR(INDEX(COGS!$B$2:$B$90000;MATCH(C2;COGS!$A$2:$A$90000;0));0)
```
- **Pivoting stock data (B column) from long to wide format by period (A column) per SKU (C column) multiplied by the price (in T column):**
``` excel
=SUMIFS('Stock history'!$B$2:$B$90000;'Stock history'!$C$2:$C$90000;$A2;'Stock history'!$A$2:$A$90000;B$1)*$T2
```
- **Percent running total. Cumulative sum of stock value in column B:**
Cell D2 formula:
``` excel
=C2
// or
=SUM($C$2:C2)
```
Cell D3 formula. Drag this formula down (right down corner double click):
``` excel
=SUM($C$2:C3)
```
- **Nested IF function with two conditions:**
``` excel
=IF(C2<=0,8;"A";IF(C2<=0,95;"B";"C"))
```
### Excel functions
- **Adds values. You can add individual values, cell references or ranges or a mix of all three:**
``` excel
SUM(number1,[number2],...)
```
- **Adds all of its arguments that meet multiple criteria. Sum many rows based on intersection of many criteria. Value 1 in column 1, value 2 in column 2 etc.:**
``` excel
SUMIFS(sum_range, criteria_range1, criteria1, [criteria_range2, criteria2], ...)
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
- **Show a certain value when error like zero `0` or empty cell `""`. Errors are a friend. They are like a pain signal giving feedback. Remove them only if you understand the analysis deeply:**
``` excel
IFERROR(value, value_if_error)
```
- **INDEX with MATCH as improved VLOOKUP (it does what VLOOKUP and more like intersection). Find value from A2 in the column of A up to A200 and show value from the same row but from column B:**
``` excel
IFERROR(INDEX(Sheet1'!$B$2:$B$200;MATCH(A2;'Sheet1'!$A$2:$A$200;0));"")
```
-  **Logical comparisons between a value and what you expect. IF statement can have two results. The first result is if your comparison is True, the second if your comparison is False:**
``` excel
IF(logical_test, value_if_true, [value_if_false])
```
### Power BI functions
- Returns the first expression that does not evaluate to BLANK. If all expressions evaluate to BLANK, BLANK is returned.:
``` excel
COALESCE(<expression>, <expression>[, <expression>]…)
```
- Returns a related value from another table. When the RELATED function performs a lookup, it examines all values in the specified table regardless of any filters that may have been applied.`RELATED(<Table>[Column])` fetches the _single value_ of `<Column>` from a table that is related to the current table via a model relationship. Conceptually it performs a lookup from the current row (row context) to the related table following the relationship path defined in the data model. It is designed to be used where a one-to-many relationship exists and you are on the **many** side (e.g., `Stock` many → `COGS` one).:
``` excel
RELATED(<column>)
```
- Returns the value for the row that meets all criteria specified by one or more search conditions. The value of `result_columnName` at the row where all pairs of `search_columnName` and `search_value` have an exact match. If there isn't a match that satisfies all the search values, BLANK or `alternateResult` (if specified) is returned. In other words, the function doesn't return a lookup value if only some of the criteria match. If multiple rows match the search values and the values in the `result_columnName` for these rows are identical, then that value is returned. However, if `result_columnName` returns different values, an error or `alternateResult` (if specified) is returned.

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
### Power Query functions
- `Csv.Document` function returns the contents of the CSV document as a table.
``` excel
Csv.Document(
    source as any,
    optional columns as any,
    optional delimiter as any,
    optional extraValues as nullable number,
    optional encoding as nullable number
) as table
```
- `Table.PromoteHeaders` function promotes the first row of values as the new column headers (i.e. column names). By default, only text or number values are promoted to headers. 
``` excel
Table.PromoteHeaders(**table** as table, optional **options** as nullable record) as table
```
- `Table.TransformColumnTypes` function returns a table by applying the transform operations to the specified columns using an optional culture.
``` excel
Table.TransformColumnTypes(
    **table** as table,
    **typeTransformations** as list,
    optional **culture** as nullable text
) as table
```
- `Table.NestedJoin` function joins the rows of `table1` with the rows of `table2` based on the equality of the values of the key columns selected by `key1` (for `table1`) and `key2` (for `table2`). The results are entered into the column named `newColumnName`. The optional `joinKind` specifies the kind of join to perform. By default, a left outer join is performed if a `joinKind` is not specified. An optional set of `keyEqualityComparers` may be included to specify how to compare the key columns. This `keyEqualityComparers` feature is currently intended for internal use only.
``` excel
Table.NestedJoin(
    table1 as table,
    key1 as any,
    table2 as any,
    key2 as any,
    newColumnName as text,
    optional joinKind as nullable number,
    optional keyEqualityComparers as nullable list
) as table
```
- `Table.ExpandTableColumn` function expands tables in `table["column"]` into multiple rows and columns. `columnNames` is used to select the columns to expand from the inner table. Specify `newColumnNames` to avoid conflicts between existing columns and new columns.
``` excel
Table.ExpandTableColumn(
    table as table,
    column as text,
    columnNames as list,
    optional newColumnNames as nullable list
) as table
```
- `Table.ReplaceValue` function replaces a value with a new value in the specified columns of a table. 
``` excel
Table.ReplaceValue(
    **table** as table,
    **oldValue** as any,
    **newValue** as any,
    **replacer** as function,
    **columnsToSearch** as list
) as table
```
- `Table.AddColumn` function adds a column named `newColumnName` to the table `table`. The values for the column are computed using the specified selection function `columnGenerator` with each row taken as an input.
``` excel
Table.AddColumn(
    **table** as table,
    **newColumnName** as text,
    **columnGenerator** as function,
    optional **columnType** as nullable type
) as table
```
### ABC analysis in Excel
#### Main formula
``` mermaid
flowchart TD
    A[Start] --> B{Is F2 <= 0,8?}
    B -- Yes --> CatA["Return 'A'"]
    B -- No --> C{Is F2 <= 0,95?}
    C -- Yes --> CatB["Return 'B'"]
    C -- No --> CatC["Return 'C'"]
    CatA --> End[End]
    CatB --> End
    CatC --> End
```
``` excel
=IF(C2<=0,8;"A";IF(C2<=0,95;"B";"C"))
```
#### Analysis execution steps
**ABC groups definition:**
A - most important SKUs
B - less important SKUs
C - not important SKUs

**Opening data:**
Double-click it or use File > Open in Excel. If Unicode characters don't display correctly, import it via Excel's Data tab > Get Data > From Text/CSV.

#### ABC analysis in Excel
1. "Stock history" table usually as ERP data dump in long format. Stock quantity at the end of the calendar month.
2. Cost of Goods Sold "COGS" table for prices.
3. Copy all SKUs and paste to "Table" sheet as values and remove duplicates. 
```
Excel -> Data -> Remove Duplicates
```
4. Add prices from "COGS" for every index via INDEX(MATCH).
5. Copy all periods from "Stock history" and remove duplicates. Paste them transposed as columns in "Table". 
6. Use SUMIFS function to populate stock value in COGS per SKU and Period.
7. For ABC analysis copy and paste value of stock for the first period to "ABC" sheet. SKU in column A and Values of stock in column B. Make a table and sort descending from Largest to Smallest value by column B. Add a new column as ratio of a particular stock in the sum of entire stock value as column C:
``` excel
B2/SUM($B$2:$B$9000)
```
8. Add cumulative SUM column as D by blocking starting cell selection:
``` excel
SUM(C$2:C2)
```
9. Assign ABC groups based on column D cumulative sum values. Pareto Analysis will be the next "ABC" column as column E:
``` excel
IF(D2<=0,8;"A";(IF(D2<=0,95;"B";"C")))
```
10. Copy SKU and ABC columns and paste them as values in the new sheet for safe keeping and repeat the ABC analysis operations. 
11. Redo the entire ABC analysis for sales data per SKU and Period. 
12. Compare ABC groups for the same periods for stock and sales. Whenever an SKU is in A in sales and C in stock it could lead to stock-out. Whenever an SKU is in C in sales and A in stock it could lead to utilization because of shelf life. 
13. Use conditional formatting for ABC classification cells with A as Green, B as Yellow and C as Red or vice versa. 
    Use `Green Fill with Dark Green Text` and `Yellow Fill with Dark Yellow Text` and `Light Red Fill with Dark Red Text`
```
Excel -> Home -> Conditional Formatting -> Highlight Cell Rules -> Text that Contains
```
### ABC analysis in Excel using Pivot Tables execution steps
1. Add corresponding "COGS" values as new column in source table using VLOOKUP or INDEX MATCH.
2. Create a new "Value" column by multiplying "COGS" by the "Stock". 
3. After selecting source table create a Pivot Table:
```
Insert -> Pivot Table -> New Worksheet
```
4. Drag "SKU" column as Rows and "Value" column as Values and sort Row Labels descending by "Value" with "More Sort Options":
```
Row Labels (Sort button click) -> More Sort Options -> Descending (Z to A) by: -> Sum of Value
```
5. Add a running total by "SKU" via "% Running Total in":
```
Sum of Value (Mouse Right click) -> Show Values As -> % Running Total In...
```
6. Select single period in the Pivot table and add a new formula based calculated column next to the Pivot table. By changing the filter we do different ABC analysis dynamically:
``` excel
=IF(B4<=0,8;"A";IF(B4<=0,95;"B";"C"))
```
## ABC analysis in Power BI
### Main formula
``` excel
ABC =
VAR CurrentPeriod = 'Stock'[Period]

// Calculate total value for the current period
VAR TotalValue =
    CALCULATE(
        SUM('Stock'[Value]),
        FILTER(
            ALL('Stock'),
            'Stock'[Period] = CurrentPeriod
        )
    )

// Determine rank of current item based on Value (descending)
VAR Ranked =
    RANKX(
        FILTER(
            ALL('Stock'),
            'Stock'[Period] = CurrentPeriod
        ),
        'Stock'[Value],
        ,
        DESC,
        Dense
    )

// Compute cumulative share of value up to current rank
VAR Cumulative =
    DIVIDE(
        SUMX(
            FILTER(
                ALL('Stock'),
                'Stock'[Period] = CurrentPeriod &&
                RANKX(
                    FILTER(ALL('Stock'), 'Stock'[Period] = CurrentPeriod),
                    'Stock'[Value],
                    ,
                    DESC,
                    Dense
                ) <= Ranked
            ),
            'Stock'[Value]
        ),
        TotalValue
    )

// Classify based on cumulative thresholds
RETURN
    IF(
        Cumulative <= 0.8,
        "A",
        IF(
            Cumulative <= 0.95,
            "B",
            "C"
        )
    )
```
#### Explanation
This captures the current row’s period and ensures that calculations are per period, not across the entire dataset:
``` excel
VAR CurrentPeriod = 'Stock'[Period]
```
Total value per period calculation. Uses ALL('Stock') to remove existing filters. Reapplies a filter to keep only the current period. Ensures the denominator of the cumulative % is the total value for that period:
``` excel
VAR TotalValue =
    CALCULATE(
        SUM('Stock'[Value]),
        FILTER(
            ALL('Stock'),
            'Stock'[Period] = CurrentPeriod
        )
    )
```
Ranking items within the period. Ranks SKUs based on their value within the current period in descending order. Dense ranking means no gaps in rank numbers (e.g., 1,2,3 even if duplicates):
``` excel
VAR Ranked =
    RANKX(
        FILTER(
            ALL('Stock'),
            'Stock'[Period] = CurrentPeriod
        ),
        'Stock'[Value],
        ,
        DESC,
        Dense
    )
```
Cumulative share calculation. Filters all rows for the current period. Keeps only items with rank ≤ current row’s rank. Sums their values, then divides by total period value. This computes the cumulative contribution of the current SKU in sorted order:
``` excel
VAR Cumulative =
    DIVIDE(
        SUMX(
            FILTER(
                ALL('Stock'),
                'Stock'[Period] = CurrentPeriod &&
                RANKX(
                    FILTER(ALL('Stock'), 'Stock'[Period] = CurrentPeriod),
                    'Stock'[Value],
                    ,
                    DESC,
                    Dense
                ) <= Ranked
            ),
            'Stock'[Value]
        ),
        TotalValue
    )
```
Classification based on thresholds for standard ABC:
``` excel
// Classify based on cumulative thresholds
RETURN
    IF(
        Cumulative <= 0.8,
        "A",
        IF(
            Cumulative <= 0.95,
            "B",
            "C"
        )
    )
```
### Analysis in Power BI execution steps
1. Load data as two separate files. Because of the common name of single column a data relation will be created. In this case we have 1 unique value in COGS column of "COGS" table and many rows for the same SKU in "Stock" table:
```
Cardinality: Many to one
```
2. Add new column of data in Stock table getting the COGS corresponding values:
``` excel
COGS = RELATED(COGS[COGS])
```
or the same but with error handling:
``` excel
COGS = 
VAR RelatedCOGS = RELATED(COGS[COGS])
RETURN
    // Use COALESCE to handle cases where no match is found for SKU
    COALESCE(RelatedCOGS, 0)

// --- Explanation ---
// RELATED: Fetches the single related value from COGS table for each SKU
// COALESCE: Replaces BLANK values with 0 if there's no matching SKU
// This column now holds the corresponding COGS amount for each Stock row.
```
3. Based on provided corresponding value per unit column (COGS) we can now calculate the value of the stock in the new column:
``` excel
Value = Stock[Stock]*Stock[COGS]
```
4. Apply the main formula to calculate the ABC classification based on 'Value' column.
5. Export Data with 30k rows limit: Create a table as visual and select it:
```
More options -> Export data
```
Export data as CSV without 150k rows limit by running the Power Query code:
``` excel
= let
    Source = #"Your Final Table",
    Export = Table.ExportCsv(Source, "C:\Exports\abc_analysis.csv")
in
    Export
```
 DAX Studio: https://daxstudio.org/. DAX Studio is the most reliable way to extract large datasets — it queries the full model directly, bypassing UI limits. Install and open DAX Studio when Power BI file is already opened and it will suggest to connect to it. DAX Studio can also explore all the hidden details of your data model, such as hidden tables, query performance etc. Once the connection is established run this command to load the data:
``` excel
EVALUATE 'Stock'
```
Then export any amount of data to CSV with the delimiter appropriate to data (character not present in the data):
```
Advanced -> Export Data -> CSV Files
```
