### Shortcuts Hotkeys:
| 🧩 **Action**                                                        | ⌨️ **Windows Shortcut**  | 🍎 **Mac Shortcut**                         | 📝 **Notes**                                        |
| :------------------------------------------------------------------- | :----------------------- | :------------------------------------------ | :-------------------------------------------------- |
| **Array formula**                                                    | `Ctrl + Shift + Enter`   | `⌃ + Shift + Return`                        | Confirms array formulas (older Excel versions).     |
| **Block cell selection with dollar symbols** _(absolute references)_ | `F4`                     | `⌘ + T` _(or `Fn + F4` on laptops)_         | Cycles `$A$1`, `A$1`, `$A1`, etc.                   |
| **Create filter**                                                    | `Ctrl + Shift + L`       | `⌃ + Shift + L` _(or `⌘ + Shift + F`)_      | Adds/removes column filters.                        |
| **Create table (structured Table)**                                  | `Ctrl + T`               | `⌘ + T`                                     | Converts range into a structured Excel Table.       |
| **Create _list-type_ table (legacy)**                                | `Ctrl + L`               | `⌃ + L`                                     | Creates a “List Object,” Excel’s older table form.  |
| **Drop-down list of existing values**                                | _(N/A)_                  | `⌥ + ↓`                                     | Shows existing entries from the column.             |
| **Edit cell**                                                        | `F2`                     | `⌃ + U`                                     | Opens cell for editing.                             |
| **Find and Replace**                                                 | `Ctrl + H`               | `⌘ + Shift + H` _(or `⌘ + F` to find only)_ | Opens the Find/Replace dialog.                      |
| **Go until the end of values**                                       | `Shift + (Arrow)`        | `Shift + (Arrow)`                           | Extends selection to data end.                      |
| **Go to section (jump to end)**                                      | `Ctrl + (Arrow)`         | `⌘ + (Arrow)`                               | Moves to edge of data region.                       |
| **Next sheet**                                                       | `Ctrl + PageDown`        | `⌘ + Option + →` _(or `Fn + ⌃ + ↓`)_        | Moves to next worksheet tab.                        |
| **Previous sheet**                                                   | `Ctrl + PageUp`          | `⌘ + Option + ←` _(or `Fn + ⌃ + ↑`)_        | Moves to previous worksheet tab.                    |
| **Repeat last action**                                               | `Ctrl + Y`               | `⌘ + Y` _(or `⌘ + Shift + Z`)_              | Repeats the last command or action.                 |
| **Select all**                                                       | `Ctrl + A`               | `⌘ + A`                                     | Selects all cells in the current data region.       |
| **Select all until the end of values**                               | `Ctrl + Shift + (Arrow)` | `⌘ + Shift + (Arrow)`                       | Selects to the end of contiguous data.              |
| **Select column**                                                    | `Ctrl + Space`           | `⌃ + Space`                                 | Selects the entire column of the active cell.       |
| **Select section (jump selection)**                                  | `Ctrl + Shift + (Arrow)` | `⌘ + Shift + (Arrow)`                       | Expands selection to data edge.                     |
| **Select object**                                                    | `Ctrl + Shift + Space`   | `⌃ + Shift + Space`                         | Selects all objects (charts, shapes, etc.)          |
| **Select row**                                                       | `Shift + Space`          | `Shift + Space`                             | Selects the entire row.                             |
| **Two decimal places + thousand separator**                          | `Ctrl + Shift + !`       | `⌘ + Shift + !`                             | Applies number format with commas and two decimals. |
| **Undo last action**                                                 | `Ctrl + Z`               | `⌘ + Z`                                     | Reverts last action.                                |
### Definitions
- **CSV** - Comma-Separated Values. The most common text data format.
- **Long and wide data format** - Long (narrow or stacked or vertical) format means each row is an observation, while wide (horizontal or unstacked) format spreads variables across columns.
- **Pivoting** - transposes the data from vertical to horizontal format. Creates columns from rows. Pivot function in Python. Cross Tab tool in Alteryx.
- **SKU** - Stock Keeping Unit. Alphanumeric symbol for a type of physical good a company uses. Basis for masterdata management.
### Techniques
- **Connecting price data from B column of "COGS" table to the stock table based on the SKUs from C column that can be found in A column of "COGS" table:**
``` excel
=IFERROR(INDEX(COGS!$B$2:$B$90000;MATCH(C2;COGS!$A$2:$A$90000;0));0)
```
- **Pivoting stock data (B column) from long to wide format by period (A column) per SKU (C column) multiplied by the price (in T column):**
``` excel
=SUMIFS('Stock history'!$B$2:$B$90000;'Stock history'!$C$2:$C$90000;$A2;'Stock history'!$A$2:$A$90000;B$1)*$T2
```
- **Cumulative sum of stock value in column B:**
Cell C1 formula:
``` excel
=C2
```
Cell C2 formula. Drag this formula down (right down corner double click):
``` excel
=SUM($C$2:C3)
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
- **Show a certain value when error like zero `0` or empty cell `""`**
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

**ABC analysis in Excel:**
1. "Stock history" table usually as ERP data dump in long format. Stock quantity at the end of the calendar month.
2. Cost of Goods Sold "COGS" table for prices.
3. Copy all SKUs and paste to "Table" sheet as values and remove duplicates. 
```
Excel -> Data -> Remove Duplicates
```
4. Add prices from "COGS" for every index via INDEX(MATCH).
5. Copy all periods from "Stock history" and remove duplicates. Paste them transposed as columns in "Table". 
6. Use SUMIFS function to populate stock value in COGS per SKU and Period.
7. Create new "Sum" column and summarize each row then copy and paste the SKU and Sum column into new sheet and sort descending from Largest to Smallest to find the most important SKUs.
8. For ABC analysis copy and paste value of stock for the first period to "ABC" sheet. Make a table and sort descending from Largest to Smallest value. Add cumulative SUM by blocking starting cell selection:
``` excel
SUM(C$2:C2)
```
9. Calculate total sum of stock in the next column to have a point of reference for the value of each stock. Divide Cumulative sum by Total sum to get the percentage for the Pareto Analysis in the next "ABC" column:
``` excel
IF(F2<=0,8;"A";(IF(F2<=0,95;"B";"C")))
```
10. Copy SKU and ABC columns and paste them as values and repeat the last point operation for each period separately or for an aggregation of periods. 
11. Redo the entire ABC analysis for sales data per SKU and Period. 
12. Compare ABC groups for the same periods for stock and sales. Whenever an SKU is in A in sales and C in stock it could lead to stock-out. Whenever an SKU is in C in sales and A in stock it could lead to utilization because of shelf life. 
13. Use conditional formatting for ABC classification cells with A as Green, B as Yellow and C as Red or vice versa. 
    Use `Green Fill with Dark Green Text` and `Yellow Fill with Dark Yellow Text` and `Light Red Fill with Dark Red Text`
```
Excel -> Home -> Conditional Formatting -> Highlight Cell Rules -> Text that Contains
```
