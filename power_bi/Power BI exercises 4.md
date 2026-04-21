# Model the Data
### Exercise 1: Implementing CALCULATE and Modifying Filter Context
**Objective:** Use DAX to establish base aggregations and manipulate their filter context using the CALCULATE function.
#### Data Input
Save the following code block as a CSV file named `Regional_Sales.csv` on your local machine.
**Code snippet:**
``` c
OrderID,Category,SalesAmount,Region
1,Furniture,500,North
2,Technology,1200,South
3,Furniture,300,South
4,Office Supplies,150,North
5,Technology,800,North
```
#### Step-by-Step Instructions
1. **Import Data:** Open Power BI Desktop. Choose **Get data > Text/CSV**, locate `Regional_Sales.csv`, and click **Load**.
2. **Create Base Measure:** Navigate to the **Data** view. Right-click the `Regional_Sales` table in the Fields pane and select **New measure**. Create the core aggregation:
    `Total Sales = SUM(Regional_Sales[SalesAmount])`
3. **Apply Single Filter Context:** Right-click the table and select **New measure**. Use CALCULATE to override the default filter context and isolate Technology sales:
    `Technology Sales = CALCULATE([Total Sales], Regional_Sales[Category] = "Technology")`
4. **Apply Multiple Filter Contexts:** Right-click the table and select **New measure**. Use CALCULATE with multiple filter arguments to isolate Technology sales specifically in the North region:
    `Tech Sales North = CALCULATE([Total Sales], Regional_Sales[Category] = "Technology", Regional_Sales[Region] = "North")`
5. **Verify Execution:** Switch to the **Report** view. Add a Matrix visual with `Region` on Rows and `Category` on Columns. Add all three measures to the Values well. Observe how the base measure respects the visual's filter context, while the CALCULATE measures override it based on your hardcoded conditions.
### Exercise 2: Iterating Functions and Context Transition
**Objective:** Utilize `SUMX` to iterate over a table and evaluate an expression row by row, contrasting it with standard aggregation.
#### Data Input
Save the following code block as a CSV file named `Product_Sales.csv`.
**Code snippet:**
``` c
ProductID,Quantity,UnitPrice
A,10,5.00
B,5,15.00
C,2,50.00
D,20,2.50
```
#### Step-by-Step Instructions
1. **Import Data:** Open Power BI Desktop. Select **Get data > Text/CSV**, locate `Product_Sales.csv`, and click **Load**.
2. **Create Standard Measure (Error Demonstration):** Navigate to the **Data** view. Right-click the `Product_Sales` table and select **New measure**. Enter:
    `Total Sales (Incorrect) = SUM(Product_Sales[Quantity]) * SUM(Product_Sales[UnitPrice])`
3. **Create Iterating Measure:** Right-click the table and select **New measure**. Use `SUMX` to enforce row-by-row calculation:
    `Total Sales (Correct) = SUMX(Product_Sales, Product_Sales[Quantity] * Product_Sales[UnitPrice])`
4. **Create Calculated Column:** Right-click the table and select **New column**. Calculate the row-level total physically:
    `Row Total = Product_Sales[Quantity] * Product_Sales[UnitPrice]`
5. **Verify Context:** Switch to **Report** view. Add a Table visual containing `ProductID`, `Total Sales (Incorrect)`, `Total Sales (Correct)`, and `Row Total`.
6. **Analyze Results:** Observe the Total row. `Total Sales (Incorrect)` multiplies the aggregate sum of quantities by the aggregate sum of unit prices, yielding an invalid overarching total. `Total Sales (Correct)` and `Row Total` correctly sum the individual row-level products.
### Exercise 3: Implementing and Marking a Date Dimension
**Objective:** Integrate a dedicated date dimension, mark it to support time intelligence, and eliminate inefficient shadow date tables .
#### Data Input
Save these code blocks as separate CSV files.
**File 1: DateDim.csv**
**Code snippet:**
``` c
Date,Year,MonthNum,MonthName,YearMonth
2023-01-01,2023,1,Jan,202301
2023-01-02,2023,1,Jan,202301
2023-01-03,2023,1,Jan,202301
```
**File 2: Sales_Data.csv**
**Code snippet:**
``` c
SalesID,OrderDate,Amount
1,2023-01-01,100
2,2023-01-02,150
3,2023-01-03,200
```
#### Step-by-Step Instructions
1. **Import Data:** Extract `DateDim.csv` and `Sales_Data.csv` into Power BI Desktop and load them into the model.
2. **Disable Shadow Tables:** Navigate to **File > Options and settings > Options**. Under **CURRENT FILE**, select **Data Load**. Uncheck **Auto date/time** in the Time Intelligence section to prevent the engine from generating hidden, model-bloating date tables . Click **OK**.
3. **Mark as Date Table:** Switch to the **Data** view. Select the `DateDim` table in the Fields pane. On the **Table tools** ribbon, click **Mark as date table** .
4. **Validate Date Column:** In the resulting dialogue box, select the `Date` column. An ID card icon will appear next to the Date field in the Fields pane, indicating successful validation.
5. **Establish Relationship:** Switch to the **Model** view. Drag the `Date` field from `DateDim` to the `OrderDate` field in `Sales_Data` to create a single-direction, one-to-many relationship .
### Exercise 4: Data Categorization for Geography and URLs
**Objective:** Apply specific data categories to text columns to ensure accurate geographic mapping and enable image rendering within visuals .
#### Data Input
Save the following code block as a CSV file named `Store_Locations.csv`.
**Code snippet:**
``` c
StoreID,City,Country,StoreImageURL
1,Paris,France,https://example.com/paris_store.jpg
2,Paris,USA,https://example.com/paris_tx_store.jpg
3,London,UK,https://example.com/london_store.jpg
```
#### Step-by-Step Instructions
1. **Import Data:** Extract `Store_Locations.csv` into Power BI Desktop and load it into the model.
2. **Access Column Tools:** Navigate to the **Data** view (or **Report** view). Select the `Store_Locations` table in the Fields pane.
3. **Categorize City:** Click the `City` column. On the ribbon, locate the **Column tools** tab. Change the **Data category** drop-down from _Uncategorized_ to _City_ . A globe icon will appear next to the field.
4. **Categorize Country:** Click the `Country` column. Change the **Data category** to _Country_. This disambiguates locations with identical city names across different countries .
5. **Categorize Image URL:** Click the `StoreImageURL` column. Change the **Data category** to _Image URL_. When this field is added to a visual (like a Table or Matrix), Power BI will render the actual image rather than displaying the text string .
6. **Alternative Method:** Switch to the **Model** view. Select the `City` field. In the Properties pane on the right, expand the **Advanced** section and change the **Data category** .
### Exercise 5: Optimizing Compression via Cardinality Reduction
**Objective:** Reduce column cardinality by splitting a composite text field into smaller components, enabling efficient VertiPaq engine compression .
#### Data Input
Save this code block as a CSV file named `Product_Log.csv`.
**Code snippet:**
``` c
LogID,ProductString,Revenue
1,Contoso | Mountain Bike | MB-200,1500
2,Contoso | Road Bike | RB-100,1200
3,Fabrikam | Mountain Bike | MB-200,1500
4,Fabrikam | Commuter | CM-50,600
```
#### Step-by-Step Instructions
1. **Import Data:** Extract `Product_Log.csv` into Power BI Desktop and select **Transform data** to open the Power Query Editor.
2. **Assess Cardinality:** Select the `ProductString` column. Note that nearly every value is unique, representing high cardinality which is expensive to store .
3. **Split the Column:** Right-click the `ProductString` header. Select **Split Column > By Delimiter...**.
4. **Configure Delimiter:** Choose **Custom** from the delimiter drop-down, enter the pipe symbol (`|`), and click **OK** .
5. **Rename Columns:** Rename the three resulting columns to `Brand`, `Category`, and `SKU`.
6. **Verify Optimization:** Observe that the `Brand` and `Category` columns now contain repeating values. This lower cardinality allows the VertiPaq engine to apply highly effective compression algorithms .
### Exercise 6: Managing Multiple Date Fields (Inactive Relationships vs. Role-Playing Dimensions)
**Objective:** Connect a fact table containing multiple date fields to a date dimension using inactive relationships and role-playing dimension tables .
#### Data Input
Save these code blocks as separate CSV files.
**File 1: Core_DateDim.csv**
**Code snippet:**
``` c
Date,Year,Month
2023-11-01,2023,Nov
2023-11-02,2023,Nov
2023-11-03,2023,Nov
2023-11-04,2023,Nov
2023-11-05,2023,Nov
```
**File 2: Fact_Fulfillment.csv**
**Code snippet:**
``` c
OrderID,OrderDate,ShipDate,Revenue
1,2023-11-01,2023-11-03,500
2,2023-11-02,2023-11-05,250
3,2023-11-03,2023-11-05,750
```
#### Step-by-Step Instructions
1. **Import Data:** Extract `Core_DateDim.csv` and `Fact_Fulfillment.csv` into Power BI Desktop. Load both into the model.
2. **Establish Active Relationship:** Navigate to the **Model** view. Drag the `Date` field from `Core_DateDim` to the `OrderDate` field in `Fact_Fulfillment`. This creates the primary, active relationship (solid line) .
3. **Establish Inactive Relationship:** Drag the `Date` field from `Core_DateDim` to the `ShipDate` field in `Fact_Fulfillment`. This creates a secondary, inactive relationship (dashed line).
4. **Evaluate Heuristic for Inactive vs. Role-Playing:** Use inactive relationships when model size constraints are strict and DAX `USERELATIONSHIP` functions will be utilized . Use role-playing dimensions when users require independent date filtering without writing complex DAX measures .
5. **Implement Role-Playing Dimension:** Switch to the **Data** view. On the **Table tools** ribbon, click **New table**. Enter the following DAX to duplicate the date table:
    `ShipDateDim = Core_DateDim`
6. **Establish Role-Playing Relationship:** Return to the **Model** view. Drag the `Date` field from the new `ShipDateDim` table to the `ShipDate` field in `Fact_Fulfillment`. This creates an active relationship specific to the shipping date .
### Exercise 7: Resolving Many-to-Many Relationships via Dimension Simplification
**Objective:** Eliminate an invalid many-to-many relationship by de-duplicating a dimension table in Power Query to establish a performant one-to-many filter path .
#### Data Input
Save these code blocks as separate CSV files.
**File 1: Dim_Customer_Dirty.csv**
**Code snippet:**
``` c
CustomerID,CustomerName,LastContactDate
101,Alpha Corp,2023-01-15
101,Alpha Corp,2023-04-20
102,Beta LLC,2023-02-10
103,Gamma Inc,2023-03-05
103,Gamma Inc,2023-06-11
```
**File 2: Fact_Transactions.csv**
**Code snippet:**
``` c
TransactionID,CustomerID,Amount
1,101,5000
2,102,1500
3,101,3000
4,103,8500
```
#### Step-by-Step Instructions
1. **Import Data:** Extract `Dim_Customer_Dirty.csv` and `Fact_Transactions.csv` into Power BI Desktop.
2. **Observe the Error State:** Navigate to the **Model** view. Drag `CustomerID` from `Dim_Customer_Dirty` to `CustomerID` in `Fact_Transactions`. Power BI triggers a many-to-many relationship warning because the dimension table contains multiple rows for the same customer . Cancel this relationship creation.
3. **Initiate Redesign:** A many-to-many relationship risks duplicate counts, omitted records, and slow report performance . Navigate to **Home > Transform data** to open the Power Query Editor .
4. **Simplify the Dimension Table:** Select the `Dim_Customer_Dirty` query. Right-click the `CustomerID` column header. Select **Remove Duplicates**. This yields a dimension table with one unique record per customer .
5. **Apply Changes:** Click **Close & Apply** on the Home tab.
6. **Establish Valid Relationship:** Return to the **Model** view. Drag `CustomerID` from the now-cleaned dimension table to the fact table. Power BI natively creates the optimal single-direction, one-to-many relationship .
### Exercise 8: Optimizing One-to-One Relationships via Merging
**Objective:** Identify a one-to-one relationship between two dimension tables and streamline the data model by merging them in the Power Query Editor .
#### Data Input
Save these code blocks as separate CSV files.
**File 1: Dim_Employee_Core.csv**
**Code snippet:**
``` c
EmployeeID,Name,Department
101,Alice,Sales
102,Bob,IT
103,Charlie,HR
```
**File 2: Dim_Employee_Details.csv**
**Code snippet:**
``` c
EmployeeID,HireDate,Location
101,2021-06-01,New York
102,2020-03-15,London
103,2022-11-10,Tokyo
```
#### Step-by-Step Instructions
1. **Import Data:** Extract `Dim_Employee_Core.csv` and `Dim_Employee_Details.csv` into Power BI Desktop and load them into the model.
2. **Observe 1:1 Relationship:** Navigate to the **Model** view. Drag `EmployeeID` from `Dim_Employee_Core` to `EmployeeID` in `Dim_Employee_Details`. Power BI creates a 1:1 bidirectional relationship .
3. **Initiate Optimization:** A one-to-one relationship signals an opportunity to simplify the data model by merging the tables into a single dimension. Navigate to **Home > Transform data**.
4. **Merge Queries:** In the Power Query Editor, select the `Dim_Employee_Core` query. On the Home ribbon, click **Merge Queries**.
5. **Configure Merge:** In the dialogue box, select `Dim_Employee_Details` as the second table. Click the `EmployeeID` column in both table previews to define the join key. Click **OK**.
6. **Expand Columns:** A new column named `Dim_Employee_Details` appears containing table objects. Click the expand icon (two diverging arrows) in the column header. Uncheck `EmployeeID` and uncheck "Use original column name as prefix". Click **OK**.
7. **Disable Secondary Load:** Right-click the `Dim_Employee_Details` query in the left pane and uncheck **Enable load**. This prevents the redundant table from loading into the Desktop model.
8. **Apply Changes:** Click **Close & Apply**. The Model view now displays a single, consolidated Employee dimension table.
### Exercise 9: Filter Flow and Cross-Filter Direction
**Objective:** Observe default single-direction filter propagation and manipulate the cross-filter direction to understand bidirectional filtering impacts .
#### Data Input
Save these code blocks as separate CSV files.
**File 1: Dim_Store.csv**
**Code snippet:**
``` c
StoreID,StoreName,Region
1,Store North,North
2,Store South,South
3,Store East,East
```
**File 2: Fact_StoreSales.csv**
**Code snippet:**
``` c
SaleID,StoreID,UnitsSold
101,1,50
102,1,75
103,2,120
104,2,40
```
#### Step-by-Step Instructions
1. **Import Data:** Extract `Dim_Store.csv` and `Fact_StoreSales.csv` into Power BI Desktop.
2. **Verify Default Direction:** Navigate to the **Model** view. Power BI automatically establishes a 1-to-many relationship. Observe the arrow on the relationship line; it points from the dimension table to the fact table, indicating a single-direction filter .
3. **Test Single-Direction Filter:** Switch to the **Report** view. Create two Table visuals. In Table A, place `StoreName`. In Table B, place `SaleID` and `UnitsSold`. Click "Store North" in Table A. Table B filters to display only SaleID 101 and 102. The selection is transmitted from the dimension to the fact table .
4. **Test Reverse Filter Failure:** Click a row in Table B (e.g., SaleID 103). Observe Table A. The `StoreName` table does not filter to "Store South" because filters do not flow upstream against the arrow's direction.
5. **Enable Bidirectional Filtering:** Return to the **Model** view. Double-click the relationship line. Change the **Cross-filter direction** drop-down from _Single_ to _Both_. Click **OK**. Arrows now point in both directions.
6. **Observe Bidirectional Impact:** Return to the **Report** view. Click SaleID 103 in Table B again. Table A now filters to display only "Store South". The filter transmits from the fact table to the dimension table.
7. **Revert to Best Practice:** Return to the **Model** view and revert the cross-filter direction to _Single_. Bidirectional relationships introduce ambiguity, risk errors, and degrade report performance . Default to single-direction relationships unless establishing specific many-to-many workarounds .
### Exercise 10: Diagnosing Disconnected Tables
**Objective:** Identify and resolve missing model relationships by observing repeating values in report visualizations .
#### Data Input
Save these code blocks as separate CSV files.
**File 1: Dim_Store_Status.csv**
**Code snippet:**
``` c
StoreID,StoreManager,Status
1,John Doe,Active
2,Jane Smith,Active
3,Bill Jones,Closed
```
**File 2: Fact_DailySales.csv**
**Code snippet:**
``` c
Date,StoreID,SalesAmount
2023-12-01,1,1500
2023-12-01,2,2200
2023-12-02,1,1800
2023-12-02,2,2400
```
#### Step-by-Step Instructions
1. **Import Data:** Extract `Dim_Store_Status.csv` and `Fact_DailySales.csv` into Power BI Desktop.
2. **Bypass Relationship Auto-Detection:** Navigate to the **Model** view. If Power BI automatically created a relationship using `StoreID`, delete it by right-clicking the relationship line and selecting **Delete**. Ensure the tables remain completely disconnected.
3. **Construct Diagnostic Visual:** Switch to the **Report** view. Add a Table visual to the canvas.
4. **Trigger the Error State:** Drag `StoreManager` from `Dim_Store_Status` and `SalesAmount` from `Fact_DailySales` into the Table visual.
5. **Observe Repeating Values:** Note that `SalesAmount` displays the exact identical grand total (7900) for every manager. Attempting to filter a fact table using a dimension table lacking a relationship forces the engine to display repeating grand totals. Do not attempt to alter visual settings to fix this.
6. **Resolve Root Cause:** Return to the **Model** view. Drag `StoreID` from `Dim_Store_Status` to `StoreID` in `Fact_DailySales` to establish the required relationship .
7. **Verify Correction:** Return to the **Report** view. The Table visual now accurately filters and distributes the sales amounts to the correct store managers.

**Author:**
Zbigniew Galar
