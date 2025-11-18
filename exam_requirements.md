### ABC Analysis execution steps
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
``` excel
IFERROR(INDEX(COGS!$B$2:$B$90000;MATCH(C2;COGS!$A$2:$A$90000;0));0)
```
5. Copy all periods from "Stock history" and remove duplicates. Paste them transposed as columns in "Table". 
6. Use SUMIFS function to populate stock value in COGS per SKU and Period.
``` excel
=SUMIFS('Stock history'!$B$2:$B$90000;'Stock history'!$C$2:$C$90000;$A2;'Stock history'!$A$2:$A$90000;B$1)
```
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
### XYZ Analysis execution steps
**XYZ groups definition:**
X - stable SKUs
Y - less stable SKUs
Z - not stable SKUs

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
