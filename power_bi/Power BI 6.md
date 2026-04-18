# Create Model Calculations Using DAX
### Exercise 1: Explicit Measures and Iterator Functions
**Objective:** Replace implicit summarization with explicit measures and compute row-context extensions using iterator functions.
#### Data Input
Save this as `Orders_Details.csv`.
**Code snippet:**
``` c
OrderID,Quantity,UnitPrice,DiscountValue
101,10,15.00,5.00
102,5,20.00,0.00
103,20,5.00,10.00
```
#### Step-by-Step Instructions
1. **Import Data:** Extract `Orders_Details.csv` into Power BI Desktop and load it to the model.
2. **Disable Implicit Measures:** Switch to Data view. Select the `Quantity`, `UnitPrice`, and `DiscountValue` columns. Change their **Summarization** property to _Don't summarize_ to prevent default aggregation by report viewers.
3. **Create Standard Measure:** Right-click the `Orders_Details` table and select **New measure**. Enter the DAX expression: `Total Quantity = SUM('Orders_Details'[Quantity])`.
4. **Create Iterator Measure:** Select **New measure** again. Use `SUMX` to calculate the net total row by row before aggregating: `Total Sales = SUMX('Orders_Details', ('Orders_Details'[Quantity] * 'Orders_Details'[UnitPrice]) - 'Orders_Details'[DiscountValue])`.
5. **Verify Calculation:** Switch to Report view. Create a Table visual containing `OrderID`, `Total Quantity`, and `Total Sales`. `Total Sales` correctly applies the mathematical extension per row.
### Exercise 2: CALCULATE and Filter Context Modification
**Objective:** Override visual filter contexts using `CALCULATE` combined with hardcoded parameters and the `REMOVEFILTERS` modifier .
#### Data Input
Save this as `Sales_Data.csv`.
**Code snippet:**
``` c
Country,Category,Sales
Germany,Beverages,100
Germany,Condiments,50
France,Beverages,200
France,Condiments,150
```
#### Step-by-Step Instructions
1. **Import Data:** Load `Sales_Data.csv` into Power BI Desktop.
2. **Base Measure:** Create the core aggregation: `Total Sales = SUM(Sales_Data[Sales])` .
3. **Apply Hardcoded Filters:** Create a measure overriding external context with explicit parameters: `Germany Beverages Sales = CALCULATE([Total Sales], Sales_Data[Country] = "Germany", Sales_Data[Category] = "Beverages")` .
4. **Remove Specific Filters:** Create a measure stripping context from a designated column: `All Countries Sales = CALCULATE([Total Sales], REMOVEFILTERS(Sales_Data[Country]))` .
5. **Verify Context Interaction:** Add a Table visual containing `Category`, `Total Sales`, `Germany Beverages Sales`, and `All Countries Sales`. Add a Slicer for `Country`.
6. **Execute Test:** Select "France" in the Slicer.
    - `Total Sales` dynamically filters to France.
    - `Germany Beverages Sales` statically returns the German Beverage value, ignoring the slicer .
    - `All Countries Sales` ignores the France slicer but dynamically respects the Category visual row context .
### Exercise 3: Implementing Time Intelligence Functions
**Objective:** Compute Year-to-Date (YTD) aggregations and historical period comparisons using DAX Time Intelligence functions.
#### Data Input
Save these code blocks as separate CSV files.
**File 1: DateDim.csv**
**Code snippet:**
``` c
Date,Year,Month
2022-01-01,2022,Jan
2022-02-01,2022,Feb
2023-01-01,2023,Jan
2023-02-01,2023,Feb
```
**File 2: Fact_Sales.csv**
**Code snippet:**
``` c
OrderDate,SalesAmount
2022-01-01,500
2022-02-01,700
2023-01-01,600
2023-02-01,850
```
#### Step-by-Step Instructions
1. **Import and Connect:** Load both tables into Power BI Desktop. Establish a single-direction, one-to-many relationship from `DateDim[Date]` to `Fact_Sales[OrderDate]`.
2. **Mark Date Table:** Time intelligence functions fail without a recognized continuous date framework. Select `DateDim` in the Data view, go to **Table tools**, and select **Mark as date table**. Select the `Date` column as the primary identifier.
3. **Create Base Measure:** Right-click `Fact_Sales` and select **New measure**: `Total Sales = SUM(Fact_Sales[SalesAmount])`.
4. **Calculate YTD:** Create a measure to aggregate sales progressively throughout the year: `YTD Sales = TOTALYTD([Total Sales], DateDim[Date])` .
5. **Calculate Historical Comparison:** Create a measure overriding the filter context to evaluate the identical period from the prior year: `Sales Last Year = CALCULATE([Total Sales], PARALLELPERIOD(DateDim[Date], -12, MONTH))` .
6. **Verify Execution:** Switch to Report view. Create a Matrix visual with `Year` and `Month` on Rows, and place `Total Sales`, `YTD Sales`, and `Sales Last Year` in the Values well. Include fields from the date table on the visual to prevent opaque, aggregate-only results .
### Exercise 4: Conditional Calculation via Scope and Filter Testing
**Objective:** Suppress irrelevant subtotals and grand totals using DAX functions `HASONEVALUE` and `ISINSCOPE` instead of visual formatting .
#### Data Input
Save this code block as `Store_Hierarchy.csv`.
**Code snippet:**
``` c
Region,City,StoreName,Sales
North,New York,Store A,500
North,New York,Store B,300
North,Boston,Store C,400
South,Atlanta,Store D,600
```
#### Step-by-Step Instructions
1. **Import Data:** Load `Store_Hierarchy.csv` into Power BI Desktop.
2. **Create Base Measure:** Right-click the table, select **New measure**, and define the core aggregation: `Total Sales = SUM(Store_Hierarchy[Sales])`.
3. **Implement HASONEVALUE:** Create a measure that evaluates only when the filter context contains exactly one distinct city:
    `City Sales Only = IF(HASONEVALUE(Store_Hierarchy[City]), [Total Sales])` .
4. **Implement ISINSCOPE:** Create a measure that executes only when the specific `StoreName` column is actively grouping the data within the visual matrix:
    `Store Level Sales = IF(ISINSCOPE(Store_Hierarchy[StoreName]), [Total Sales])` .
5. **Verify Matrix Behavior:** Switch to Report view. Create a Matrix visual. Place `Region`, `City`, and `StoreName` into the Rows well to form a hierarchy. Place `Total Sales`, `City Sales Only`, and `Store Level Sales` into the Values well.
6. **Analyze Scope Resolution:** Expand all hierarchy levels in the Matrix.
    - `Total Sales` calculates at all granularities, including the grand total.
    - `City Sales Only` returns blank at the Region subtotal and Grand Total levels because multiple cities exist in those contexts .
    - `Store Level Sales` returns blank at the Region, City, and Grand Total levels; it exclusively calculates for the individual StoreName rows where the field is strictly in scope.
### Exercise 5: Auto-Generating DAX via Quick Measures
**Objective:** Jump-start DAX creation using the Quick measure wizard, mapping field inputs to auto-generated syntax, and resolving default naming conventions .
#### Data Input
Save this code block as `Product_Net.csv`.
**Code snippet:**
``` c
ProductID,Category,NetValue
101,Furniture,500
102,Furniture,300
103,Technology,1200
104,Technology,800
```
#### Step-by-Step Instructions
1. **Import Data:** Load `Product_Net.csv` into Power BI Desktop.
2. **Initiate Wizard:** Switch to the Data view. In the Fields pane, select the `Product_Net` table, right-click, and choose **Quick measure** to ensure the new measure is housed within the correct table .
3. **Configure Calculation Type:** In the Quick measure dialogue box, open the **Calculation** drop-down and select _Average per category_ .
4. **Map Data Fields:** Drag `NetValue` from the Fields list on the right into the **Base value** well on the left. Drag `Category` into the **Category** well . Click **OK**.
5. **Inspect Generated DAX:** Click the newly created measure in the Fields pane. Observe the Formula Bar to review the DAX code the wizard authored . Identify the underlying functions (e.g., `CALCULATE`, `KEEPFILTERS`).
6. **Rename Artifact:** The wizard generates cumbersome names based on the inputs (e.g., _NetValue average per Category_). Edit the Formula Bar text before the equals sign to rename it to `Avg Category Value` .
### Exercise 6: Implementing Statistical DAX Functions
**Objective:** Compute core statistical metrics to evaluate data distribution using dedicated DAX statistical functions .
#### Data Input
Save this code block as `Store_Traffic.csv`.
**Code snippet:**
``` c
Date,StoreName,DailyVisitors
2023-10-01,Store A,250
2023-10-02,Store A,260
2023-10-03,Store A,245
2023-10-04,Store A,900
2023-10-05,Store A,255
```
#### Step-by-Step Instructions
1. **Import Data:** Load `Store_Traffic.csv` into Power BI Desktop.
2. **Calculate Mean:** Right-click the table, select **New measure**, and define the average:
    `Average Visitors = AVERAGE(Store_Traffic[DailyVisitors])` .
3. **Calculate Median:** Select **New measure** and compute the exact midpoint of the distribution to mitigate the impact of extreme outliers:
    `Median Visitors = MEDIAN(Store_Traffic[DailyVisitors])` .
4. **Calculate Variance (Standard Deviation):** Select **New measure** and calculate the dispersion of visitors from the mean (treating the data as a complete population):
    `Visitor Deviation = STDEV.P(Store_Traffic[DailyVisitors])` .
5. **Analyze Statistical Variance:** Switch to the Report view. Add a Card visual for each of the three measures.
6. **Interpret Results:** Observe the disparity between the `Average Visitors` and `Median Visitors`. The single extreme outlier (900 visitors on 10-04) significantly skews the average upwards, while the median remains anchored to the typical daily volume. The `Visitor Deviation` outputs a high value, mathematically confirming extreme volatility within the dataset.
