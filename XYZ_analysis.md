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
### Excel Functions
- Adds values. You can add individual values, cell references or ranges or a mix of all three:
``` excel
SUM(number1,[number2],...)
```
- Find things in a table or a range by row. Value you want to look up must be in the first column of the range. The column number that contains the return value. Use last value as 0 for exact match:
``` excel
VLOOKUP (lookup_value, table_array, col_index_num, [range_lookup])
```
- Look in one column for a search term and return a result from the same row in another column, regardless of which side the return column is on:
``` excel
XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found], [match_mode], [search_mode])
```
- Searches for a specified item in a range of cells, and then returns the relative position of that item in the range:
``` excel
MATCH(lookup_value, lookup_array, [match_type])
```
- Returns a value or the reference to a value from within a table or range:
``` excel
INDEX(array, row_num, [column_num])
```
- Show a certain value when error like zero `0` or empty cell `""`
``` excel
IFERROR(value, value_if_error)
```
- INDEX with MATCH as improved VLOOKUP (it does what VLOOKUP and more like intersection). Find value from A2 in the column of A up to A200 and show value from the same row but from column B:
``` excel
IFERROR(INDEX(Sheet1'!$B$2:$B$200;MATCH(A2;'Sheet1'!$A$2:$A$200;0));"")
```
- Adds all of its arguments that meet multiple criteria. Sum many rows based on intersection of many criteria. Value 1 in column 1, value 2 in column 2 etc.:
``` excel
SUMIFS(sum_range, criteria_range1, criteria1, [criteria_range2, criteria2], ...)
```
-  Logical comparisons between a value and what you expect. IF statement can have two results. The first result is if your comparison is True, the second if your comparison is False:
``` excel
IF(logical_test, value_if_true, [value_if_false])
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
X - stable SKUs
Y - less stable SKUs
Z - not stable SKUs

**Opening data:**
Double-click it or use File > Open in Excel. If Unicode characters don't display correctly, import it via Excel's Data tab > Get Data > From Text/CSV.

**XYZ analysis in Excel:**
1. "Stock history" table usually as ERP data dump in long format. Stock quantity at the end of the calendar month.
2. Cost of Goods Sold "COGS" table for prices.
3. Copy all SKUs and paste to "Table" sheet as values and remove duplicates. 
```
Excel -> Data -> Remove Duplicates
```
1. Add prices from "COGS" for every index via VLOOKUP.
2. Copy all periods from "Stock history" and remove duplicates. Paste them transposed as columns in "Table". 
3. Use SUMIFS function to populate stock value in COGS per SKU and Period.
4. Create new "Sum" column and summarize each row then copy and paste the SKU and Sum column into new sheet and sort descending from Largest to Smallest to find the most important SKUs.
5. For XYZ analysis calculate coefficient of variation as new column and we use population standard deviation because we use whole history:
``` excel
IF(AVERAGE(C3:T3)=0;0;STDEV.P(C3:T3)/AVERAGE(C3:T3))
or 
IFERROR(STDEV.P(C3:T3)/AVERAGE(C3:T3);0)
```
6. Select CV column and create a histogram chart in "Charts" sheet to find the best boundary conditions for XYZ groups.
7. For XYZ analysis calculate XYZ groups as new column:
``` excel
IF(U2<=2,16;"X";(IF(U2<=2,4;"Y";"Z")))
```
8. Use conditional formatting for XYZ classification cells with X as Green, Y as Yellow and Z as Red or vice versa. 
```
Excel -> Home -> Conditional Formatting -> Highlight Cell Rules -> Text that Contains
```
