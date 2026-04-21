# Develop a Data Model
### Exercise 1: Implementing Iterating Calculated Columns with DAX
**Objective:** Create calculated columns using DAX to perform row-by-row (iterating) calculations when original data lacks subtotals or net totals .
#### Data Input
Save the following code block as a CSV file named `Orders_Details.csv`.
**Code snippet:**
``` c
OrderID,ProductID,UnitPrice,Quantity,Discount
10508,39,18.00,10,0.00
10521,35,18.00,3,0.10
10530,76,25.00,50,0.05
10546,35,18.00,30,0.00
```
#### Step-by-Step Instructions
1. **Import Data:** Extract `Orders_Details.csv` into Power BI Desktop and select **Load**.
2. **Access Data View:** Click the **Data** view icon on the left navigation bar. Select the `Orders_Details` table in the Fields pane.
3. **Calculate Subtotal:** On the **Table tools** ribbon, select **New column** . Enter the following DAX expression in the Formula Bar and press Enter: `Subtotal = 'Orders_Details'[UnitPrice] * 'Orders_Details'[Quantity]`
4. **Calculate Discount Value:** Select **New column** again. Calculate the physical discount amount:
    `Discountvalue = 'Orders_Details'[Subtotal] * 'Orders_Details'[Discount]`
5. **Calculate Line Total:** Select **New column** a final time to compute the net total:
    `LineTotal = 'Orders_Details'[Subtotal] - 'Orders_Details'[Discountvalue]`
6. **Verify Iteration:** Observe the table preview. The DAX expressions execute row by row, ensuring accurate extensions for each line item prior to aggregation .
### Exercise 2: Constructing Hierarchies and Securing Filter Paths
**Objective:** Build a structural hierarchy within a dimension table and explicitly hide foreign keys in the fact table to force accurate dimensional filtering .
#### Data Input
Save these code blocks as separate CSV files.
**File 1: Dim_Merchandise.csv**
**Code snippet:**
``` c
ProductKey,Category,Subcategory,ProductName
1,Clothing,Shirts,Blue T-Shirt
2,Clothing,Pants,Denim Jeans
3,Accessories,Hats,Baseball Cap
```
**File 2: Fact_RetailSales.csv**
**Code snippet:**
``` c
SalesID,ProductKey,Amount
101,1,20.00
102,1,20.00
103,2,50.00
104,3,15.00
```
#### Step-by-Step Instructions
1. **Import Data:** Extract `Dim_Merchandise.csv` and `Fact_RetailSales.csv` into Power BI Desktop and load them into the model. Ensure a one-to-many relationship exists between `ProductKey` in both tables.
2. **Initiate Hierarchy:** Navigate to the **Model** view. In the `Dim_Merchandise` table, right-click the `Category` field and select **Create hierarchy** . The field renames to `Category Hierarchy`.
3. **Add Hierarchy Levels:** On the Properties pane (with the hierarchy selected), use the **Select a column to add level...** dropdown to add `Subcategory`, followed by `ProductName` . Click **Apply Level Changes**.
4. **Hide Fact Table Keys:** Locate the `ProductKey` field within the `Fact_RetailSales` table. Right-click the field and select **Hide in report view** (indicated by an eye with a slash through it) .
5. **Verify Design:** Switch to the **Report** view. Expand the `Fact_RetailSales` table in the Fields pane. The `ProductKey` is invisible to report consumers. This architectural choice eliminates ambiguity and forces users to utilize the `Dim_Merchandise` hierarchy for visualizations .
### Exercise 3: Implementing Static Row-Level Security (RLS)
**Objective:** Restrict report data visibility by creating a security role with a DAX filter and validate it using the Desktop testing tools .
#### Data Input
Save this code block as a CSV file named `Global_Sales.csv`.
**Code snippet:**
``` c
SaleID,Country,Revenue
1,Germany,5000
2,France,3000
3,Germany,1500
4,USA,8000
```
#### Step-by-Step Instructions
1. **Import Data:** Extract `Global_Sales.csv` into Power BI Desktop and load it.
2. **Access Role Manager:** On the **Modeling** ribbon, click **Manage roles**.
3. **Create Role:** In the Manage roles dialogue box, click **Create** under the Roles section. Name the new role `Germany Account Manager`.
4. **Define DAX Filter:** Select the `Global_Sales` table in the middle pane. In the Table filter DAX expression pane on the right, enter the following expression to restrict access to German records:
    `[Country] = "Germany"`
5. **Save Role:** Click **Save** at the bottom of the dialogue box.
6. **Establish Baseline:** Switch to the **Report** view. Create a Table visual containing `Country` and `Revenue`. The visual displays all countries and the unrestricted total revenue.
7. **Test Security Implementation:** On the **Modeling** ribbon, click **View as**. Check the box next to `Germany Account Manager` and click **OK** .
8. **Verify Restriction:** Observe the Table visual. It exclusively displays data for Germany, and a yellow banner at the top of the canvas confirms the active role . Click **Stop viewing** in the banner to return to the default developer view.
### Exercise 4: Implementing Dynamic Row-Level Security (RLS)
**Objective:** Construct a dynamic security model by mapping User Principal Names (UPNs) to specific data attributes and restricting access using the `USERPRINCIPALNAME()` DAX function .
#### Data Input
Save the following four code blocks as separate CSV files on your local machine. Replace the `@test.com` emails with your actual Power BI login email for testing purposes.
**File 1: Sec_UserUPN.csv**
**Code snippet:**
``` c
UserID,FullName,UPN
1,Megan Bowen,meganb@test.com
2,Adele Vance,adelev@test.com
```
**File 2: Sec_UserBrand.csv**
**Code snippet:**
``` c
UserID,Brand
1,Contoso
1,Litware
2,Fabrikam
```
**File 3: Dim_Product.csv**
**Code snippet:**
``` c
ProductID,Brand,ProductName
101,Contoso,Contoso Phone
102,Litware,Litware Laptop
103,Fabrikam,Fabrikam Camera
104,Proseware,Proseware Tablet
```
**File 4: Fact_Sales.csv**
**Code snippet:**
``` c
SaleID,ProductID,Revenue
1,101,500
2,102,1200
3,103,800
4,104,300
```
#### Step-by-Step Instructions
1. **Import Data:** Extract all four CSV files into Power BI Desktop and load them into the model.
2. **Establish Security Relationships:** Navigate to the **Model** view. Create the necessary filter paths for dynamic security :
    - Drag `UserID` from `Sec_UserUPN` to `UserID` in `Sec_UserBrand` (1-to-Many).
    - Drag `Brand` from `Dim_Product` to `Brand` in `Sec_UserBrand` (1-to-Many).
    - Drag `ProductID` from `Dim_Product` to `ProductID` in `Fact_Sales` (1-to-Many).
3. **Configure Cross-Filtering:** By default, filters flow from the dimension (`Dim_Product`) to the fact table. To allow the security tables to filter the products, double-click the relationship between `Dim_Product` and `Sec_UserBrand`. Change the **Cross-filter direction** to `Both` and check **Apply security filter in both directions**.
4. **Create the Dynamic Role:** On the **Modeling** ribbon, click **Manage roles**. Click **Create** and name the role `Dynamic User`.
5. **Define the DAX Filter:** Select the `Sec_UserUPN` table. In the Table filter DAX expression pane, enter:
    `[UPN] = USERPRINCIPALNAME()`
6. **Save Role:** Click **Save**. This explicitly declares that the user's access is determined by evaluating their login credential against the UPN table.
7. **Test the Configuration:** Switch to the **Report** view. Create a Table visual displaying `Brand` and `Revenue`. It will show all four brands.
8. **View as Specific User:** On the **Modeling** ribbon, click **View as**. Check the `Other user` box and type `meganb@test.com`. Check the `Dynamic User` role box. Click **OK** . The visual will securely restrict to display only "Contoso" and "Litware" .
### Exercise 5: Managing Summarization and Q&A Synonyms
**Objective:** Disable inappropriate default numeric aggregations on identifier columns and configure natural language synonyms to optimize the Q&A visual .
#### Data Input
Save the following code block as a CSV file named `Customer_Metrics.csv`.
**Code snippet:**
``` c
CustomerID,SignupYear,TotalSpend,Location
1001,2021,500.00,New York
1002,2022,1200.50,London
1003,2021,340.00,Paris
1004,2023,890.25,Tokyo
```
#### Step-by-Step Instructions
1. **Import Data:** Extract `Customer_Metrics.csv` into Power BI Desktop and load it into the model.
2. **Observe Default Summarization:** Switch to the **Data** view. In the Fields pane, note the sigma symbol ($\Sigma$) next to `CustomerID`, `SignupYear`, and `TotalSpend` . Power BI defaults to summing all numeric columns .
3. **Disable Inappropriate Aggregation:** Select the `CustomerID` column. On the **Column tools** ribbon, click the **Summarization** dropdown and change it from _Sum_ to _Don't summarize_ . Repeat this exact process for the `SignupYear` column. Leave `TotalSpend` as _Sum_.
4. **Access Q&A Setup:** Switch to the **Model** view. On the **Modeling** ribbon, click **Q&A setup** .
5. **Configure Synonyms:** In the Q&A setup window, click **Field synonyms** on the left navigation pane .
6. **Add Business Terminology:** Locate the `TotalSpend` field within the `Customer_Metrics` table. Add alternative business terms such as `revenue`, `sales`, and `income` to the synonyms list .
7. **Alternative Synonym Method:** Close the Q&A setup. Ensure the Properties pane is open in the Model view. Select the `Location` field. In the Properties pane under **Synonyms**, type `city, region` .
8. **Verify Q&A:** Switch to the **Report** view. Double-click the blank canvas to spawn a Q&A visual . Type "total sales by city" to verify the engine successfully translates the synonyms to the actual `TotalSpend` and `Location` fields.
### Exercise 6: Generating Calculated Tables with DAX
**Objective:** Construct a calculated table via DAX for immediate model availability, and identify its architectural footprint and limitations.
#### Data Input
Save this code block as a CSV file named `Customers.csv`.
**Code snippet:**
``` c
CustomerID,CustomerName,Region
1,Alpha Corp,North
2,Beta LLC,South
3,Gamma Inc,East
```
#### Step-by-Step Instructions
1. **Import Data:** Extract `Customers.csv` into Power BI Desktop and load it into the model.
2. **Initiate Table Creation:** Switch to the **Data** view. On the **Table tools** ribbon, click **New table** .
3. **Write DAX Expression:** In the Formula Bar, enter the DAX syntax to generate an exact copy of the imported table:
    `CopyofCustomers = 'Customers'`.
4. **Execute and Verify:** Press Enter. Observe the Fields pane; the new `CopyofCustomers` table features a calculator icon superimposed on the standard table icon, visually distinguishing it as a DAX-generated artifact .
5. **Evaluate Architectural Trade-offs:** Calculated tables compute during model initiation and do not recalculate dynamically during user interaction . They suffer from inferior VertiPaq engine compression compared to native Power Query tables. Use calculated tables exclusively when upstream data source modifications or Power Query transformations are strictly impossible.
### Exercise 7: Configuring Q&A Suggestions and Teaching the Engine
**Objective:** Pre-populate the Q&A visual with guided queries and train the linguistic schema to recognize custom business terminology .
#### Data Input
Save this code block as a CSV file named `Staff_Data.csv`.
**Code snippet:**
``` c
EmployeeID,FullName,TenureYears,Department
1,Alice Smith,5,Sales
2,Bob Jones,2,IT
3,Charlie Brown,10,Sales
4,Diana Prince,8,HR
```
#### Step-by-Step Instructions
1. **Import Data:** Extract `Staff_Data.csv` into Power BI Desktop and load it into the model.
2. **Deploy Visual:** Switch to the **Report** view. Double-click the blank canvas to instantiate a Q&A visual .
3. **Access Setup:** On the **Modeling** ribbon, click **Q&A setup** .
4. **Suggest Questions:** Select **Suggest questions** in the left navigation pane . Enter `who has the highest tenure years` and click **Add**. This hardcodes a clickable prompt into the default visual state to guide user exploration .
5. **Teach Q&A:** Select **Teach Q&A** in the left pane . Enter `who are the veterans` in the question box.
6. **Define Terminology:** The engine will flag "veterans" as unrecognized. In the resulting definition section, map the term to the data model by defining "veterans" as `Staff_Data[TenureYears] > 5`. Click **Save** .
7. **Verify Training:** Close the Q&A setup window. In the Q&A visual, click your suggested question to test it. Next, type `who are the veterans` to verify the engine correctly translates the taught term into the underlying DAX filter.
### Exercise 8: Advanced Data Categorization for Spatial and Visual Context
**Objective:** Apply distinct data categories to geographical data and web links to resolve spatial mapping ambiguity, enable Q&A locational queries, and force the engine to render physical images .
#### Data Input
Save the following code block as a CSV file named `Store_Directory.csv`.
**Code snippet:**
``` c
StoreID,State,PostalCode,StoreFrontImage
1,WA,98052,https://example.com/store1.jpg
2,CA,90210,https://example.com/store2.jpg
3,NY,10001,https://example.com/store3.jpg
```
#### Step-by-Step Instructions
1. **Import Data:** Extract `Store_Directory.csv` into Power BI Desktop. Select **Transform data** to open the Power Query Editor.
2. **Enforce Text Data Types for Geography:** Select the `PostalCode` column. Power Query will likely auto-detect this as a Whole Number. Click the data type icon in the header and change it to **Text**. Postal codes must be stored as text strings to be eligible for geographic categorization . Click **Close & Apply**.
3. **Categorize State:** Switch to the **Data** view. Select the `State` column. On the **Column tools** ribbon, change the **Data category** to _State or Province_. This explicitly defines the geographic entity, resolving potential mapping ambiguity (e.g., differentiating the state of Washington from Western Australia) .
4. **Categorize Postal Code:** Select the `PostalCode` column. Change its **Data category** to _Postal code_. A globe icon will appear next to both geographic fields.
5. **Categorize Image URL:** Select the `StoreFrontImage` column. Change its **Data category** to _Image URL_. When placed in a visual, this setting forces Power BI to fetch and render the actual image file rather than displaying the raw hyperlink text .
6. **Verify Q&A Integration:** Switch to the **Report** view. Double-click the canvas to spawn a Q&A visual. Type `where are the stores`. The Q&A engine successfully maps the "where" interrogative directly to your newly categorized geographic columns to generate a spatial response.

**Author:**
Zbigniew Galar
