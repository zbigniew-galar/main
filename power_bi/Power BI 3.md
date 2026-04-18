# Clean, Transform, and Load the Data
### Exercise 1: Constructing a Star Schema Data Model
**Objective:** Build a foundational star schema by establishing one-to-many relationships between dimension and fact tables and configuring single-direction cross-filtering.
#### Data Input
Save the following three code blocks as separate CSV files on your local machine.
**File 1: Dim_Product.csv**
**Code snippet:**
``` c
ProductID,ProductName,Category
101,Widget Alpha,Widgets
102,Widget Beta,Widgets
201,Gizmo X,Gizmos
```
**File 2: Dim_Date.csv**
**Code snippet:**
``` c
DateKey,Year,Month
2023-10-01,2023,October
2023-10-02,2023,October
2023-10-03,2023,October
```
**File 3: Fact_Sales.csv**
**Code snippet:**
``` c
SalesID,DateKey,ProductID,Revenue
1,2023-10-01,101,150.00
2,2023-10-01,201,300.00
3,2023-10-02,102,250.00
4,2023-10-03,101,150.00
```
#### Step-by-Step Instructions
1. **Import Data:** Open Power BI Desktop. Choose **Get data > Text/CSV**. Extract `Dim_Product.csv`, `Dim_Date.csv`, and `Fact_Sales.csv`. Click **Load** for each.
2. **Access Model View:** Click the **Model** icon on the left navigation bar.
3. **Establish Product Relationship:** Click and hold `ProductID` in the `Dim_Product` table. Drag and drop it directly onto `ProductID` in the `Fact_Sales` table.
4. **Establish Date Relationship:** Click and hold `DateKey` in the `Dim_Date` table. Drag and drop it directly onto `DateKey` in the `Fact_Sales` table.
5. **Verify Cardinality and Direction:** Double-click the relationship line connecting `Dim_Product` and `Fact_Sales`.
    - Ensure **Cardinality** is set to `Many to one (*:1)` or `One to many (1:*)` depending on selection order. The `1` side must be on the Dimension table.
    - Ensure **Cross-filter direction** is set to `Single`.
    - Click **OK**.
6. **Visual Organization:** Position `Fact_Sales` at the bottom of the canvas. Place `Dim_Product` and `Dim_Date` above it. This visual layout accurately represents the "waterfall" flow of filters from dimension tables down to the fact table.
### Exercise 2: Role-Playing Dimensions and Inactive Relationships
**Objective:** Manage multiple relationships between a fact table and a dimension table using inactive relationships and the `USERELATIONSHIP` DAX function.
#### Data Input
Save these code blocks as CSV files.
**File 1: Dim_Date_Role.csv**
**Code snippet:**
``` c
DateKey,Year,Month
2023-11-01,2023,November
2023-11-05,2023,November
2023-11-10,2023,November
```
**File 2: Fact_Orders.csv**
**Code snippet:**
``` c
OrderID,OrderDateKey,ShipDateKey,Amount
101,2023-11-01,2023-11-05,500
102,2023-11-01,2023-11-10,300
103,2023-11-05,2023-11-10,750
```
#### Step-by-Step Instructions
1. **Import Data:** Extract `Dim_Date_Role.csv` and `Fact_Orders.csv` into Power BI Desktop.
2. **Create Active Relationship:** In Model view, drag `DateKey` from `Dim_Date_Role` to `OrderDateKey` in `Fact_Orders`. This creates the primary, active relationship (solid line).
3. **Create Inactive Relationship:** Drag `DateKey` from `Dim_Date_Role` to `ShipDateKey` in `Fact_Orders`. This creates a secondary, inactive relationship (dashed line).
4. **Build Default Measure:** Switch to Data view. Create a base measure for total amount:
    `Total Amount = SUM(Fact_Orders[Amount])`
    _This measure automatically uses the active relationship (Order Date)._
5. **Build Role-Playing Measure:** Create a second measure activating the ship date relationship:
    `Amount by Ship Date = CALCULATE([Total Amount], USERELATIONSHIP(Dim_Date_Role[DateKey], Fact_Orders[ShipDateKey]))`
6. **Verify Model:** Add a matrix visual. Place `Dim_Date_Role[DateKey]` on rows. Add both measures to values. Observe how `Total Amount` aggregates by order date, while `Amount by Ship Date` aggregates by ship date using the exact same date dimension table.
### Exercise 3: Creating and Navigating Hierarchies
**Objective:** Build a geographical hierarchy within a dimension table to enable drill-down functionality in report visualizations.
#### Data Input
Save this code block as a CSV file named `Dim_Location.csv`.
**Code snippet:**
``` c
LocationID,Country,State,City
1,USA,California,Los Angeles
2,USA,California,San Francisco
3,USA,Texas,Austin
4,Canada,Ontario,Toronto
5,Canada,British Columbia,Vancouver
```
#### Step-by-Step Instructions
1. **Import Data:** Extract `Dim_Location.csv` into Power BI Desktop and click **Load**.
2. **Access Data View:** Click the **Data** view icon on the left navigation bar.
3. **Initiate Hierarchy:** In the Fields pane on the right, right-click the `Country` field and select **Create hierarchy**. A new field named `Country Hierarchy` will appear.
4. **Add Levels:** Right-click the `State` field, select **Add to hierarchy**, and choose `Country Hierarchy`. Repeat this exact process for the `City` field.
5. **Test Drill-Down:** Switch to the **Report** view icon on the left navigation bar. Add a Matrix visual to the canvas.
6. **Configure Matrix:** Drag the new `Country Hierarchy` field into the **Rows** bucket of the visual. Drag `LocationID` into the **Values** bucket (ensure it is set to Count).
7. **Navigate:** Hover over the Matrix visual and use the drill-down arrows (the split arrow icon) at the top of the visual to expand the data from Country, down to State, and finally to City.
### Exercise 4: Resolving Many-to-Many Relationships Using a Bridge Table
**Objective:** Implement a bridge table to resolve a many-to-many relationship and establish unambiguous filter paths.
#### Data Input
Save these code blocks as separate CSV files.
**File 1: Dim_Student.csv**
**Code snippet:**
``` c
StudentID,StudentName
1,Alice
2,Bob
3,Charlie
```
**File 2: Dim_Class.csv**
**Code snippet:**
``` c
ClassID,ClassName
101,Math
102,Science
```
**File 3: Bridge_StudentClass.csv**
**Code snippet:**
``` c
StudentID,ClassID
1,101
1,102
2,101
3,102
```
#### Step-by-Step Instructions
1. **Import Data:** Extract `Dim_Student.csv`, `Dim_Class.csv`, and `Bridge_StudentClass.csv` into Power BI Desktop.
2. **Access Model View:** Navigate to the Model tab.
3. **Position Tables:** Place `Bridge_StudentClass` centrally between `Dim_Student` and `Dim_Class`.
4. **Establish Relationships:** Drag `StudentID` from `Dim_Student` to `Bridge_StudentClass`. Drag `ClassID` from `Dim_Class` to `Bridge_StudentClass`.
5. **Configure Cardinality:** Verify both relationships are One-to-Many (`1:*`), flowing outward from the Dimension tables into the Bridge table.
6. **Configure Cross-Filtering:** Double-click the relationship between `Dim_Class` and `Bridge_StudentClass`. Set **Cross-filter direction** to `Both`.
7. **Verify Resolution:** Switch to Report view. Create a Matrix visual with `ClassName` on Rows and `StudentName` on Values. The bridge table correctly maps students to classes without creating an unsupported native many-to-many relationship.
