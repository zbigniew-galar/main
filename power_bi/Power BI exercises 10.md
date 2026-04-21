# Identify Patterns and Trends
### Exercise 1: Implementing Analytics Lines
**Objective:** Apply trend and average lines to reveal data clustering and identify outliers .
#### Data Input
Save this code block as `Monthly_Volume.csv`.
**Code snippet:**
``` c
Date,Sales
2023-01-01,150000
2023-02-01,160000
2023-03-01,550000
2023-04-01,145000
2023-05-01,165000
```
#### Step-by-Step Instructions
1. **Import Data:** Load `Monthly_Volume.csv` into Power BI Desktop.
2. **Construct Visual:** Create a scatter plot or line chart .
3. **Access Analytics:** Navigate to the **Analytics** pane within the Visualizations panel .
4. **Apply Trend Line:** Toggle **Trend line** to _On_ .
5. **Isolate Outliers:** Toggle **Average line** to _On_ to explicitly highlight data points breaking the dominant clustering pattern (e.g., the 550,000 value in March) .
### Exercise 2: Generating Automated Insights
**Objective:** Execute the Analyze feature to automatically process the data model and explain visual fluctuations .
#### Data Input
Use the `Monthly_Volume.csv` data from Exercise 1.
#### Step-by-Step Instructions
1. **Render Visual:** Ensure the line chart from Exercise 1 is active .
2. **Trigger AI Analysis:** Right-click the March spike (550,000) on the canvas. Select **Analyze > Explain the increase** .
3. **Review Output:** The engine evaluates relationships and generates corresponding insight visuals .
4. **Persist Insight:** Click the **+** icon in the upper right-hand corner of a useful generated visualization to permanently append it to your report page .
### Exercise 3: Modifying Axis Continuity
**Objective:** Convert a continuous time axis to a categorical axis to enable custom chronological sorting by metric value .
#### Data Input
Save this code block as `Annual_Sales.csv`.
**Code snippet:**
``` c
Year,Category,TotalSales
2018,Computers,50000
2019,Computers,120000
2020,Computers,80000
```
#### Step-by-Step Instructions
1. **Construct Baseline:** Create a column chart using `Year` on the X-axis and `TotalSales` on the Y-axis .
2. **Access Axis Properties:** Navigate to **Format visual > X-axis** .
3. **Override Continuity:** Change the **Type** dropdown from _Continuous_ to _Categorical_ .
4. **Apply Custom Sort:** Click the visual's ellipsis menu. Select **Sort by > TotalSales** and set it to **Sort descending** to rank years by volume rather than sequence .
### Exercise 4: Constructing Manual Groups
**Objective:** Consolidate discrete data points into custom groups via canvas selection and map them to interactive slicers .
#### Data Input
Save this code block as `Regional_Performance.csv`.
**Code snippet:**
``` c
Region,Revenue
North,500
South,150
East,600
West,120
```
#### Step-by-Step Instructions
1. **Build Canvas Element:** Create a column chart displaying `Revenue` by `Region`.
2. **Execute Multi-Select:** Hold the **Shift** key and click the columns for "South" and "West" .
3. **Generate Group:** Right-click the selected columns and choose **Group data**.
4. **Edit Group Metadata:** In the Fields pane, click the ellipsis next to the newly generated group and select **Edit groups** .
5. **Refine Naming:** Rename the group to `Below Target` to optimize legend clarity .
6. **Implement Filtering:** Drag the configured group field directly into a Slicer visual to enable mass filtering .
### Exercise 5: Creating Data Bins for Calculated Columns
**Objective:** Segment continuous numeric data into discrete, equally sized intervals (bins) to analyze frequency distributions .
#### Data Input
Save this code block as `Sales_Distribution.csv`.
**Code snippet:**
``` c
OrderID,TotalSalesCC
1,150.50
2,299.99
3,50.00
4,1050.75
5,800.00
6,350.25
7,99.99
8,450.00
```
#### Step-by-Step Instructions
1. **Import Data:** Load `Sales_Distribution.csv` into Power BI Desktop.
2. **Initiate Binning:** In the Fields pane, right-click the `TotalSalesCC` numeric column and select **New group** .
3. **Configure Bin Type:** In the Groups dialogue box, ensure the **Group type** is set to _Bin_ .
4. **Define Bin Logic:** Change the **Bin type** dropdown to _Number of bins_ .
5. **Set Parameter:** Enter `5` in the **Bin count** field to explicitly force the engine to split the data into five equal segments. Click **OK** .
6. **Construct Distribution Visual:** Switch to the Report view. Create a Column chart.
7. **Map Fields:** Drag the newly generated `TotalSalesCC (bins)` field onto the X-axis .
8. **Calculate Frequency:** Drag `OrderID` onto the Y-axis. Click its dropdown in the field well and change the implicit measure to **Count (Distinct)**. The visual now explicitly displays the volume of orders falling within each sales bracket .
### Exercise 6: Executing Automated Clustering
**Objective:** Leverage built-in machine learning to automatically detect statistical similarities and assign data points to distinct profiles .
#### Data Input
Save this code block as `Store_Performance.csv`.
**Code snippet:**
``` c
StoreName,TotalSales
Store A,500000
Store B,520000
Store C,100000
Store D,120000
Store E,800000
```
#### Step-by-Step Instructions
1. **Import Data:** Load `Store_Performance.csv` into Power BI Desktop.
2. **Establish Baseline Table:** Create a Table visual on the canvas containing `StoreName` and `TotalSales` .
3. **Trigger ML Algorithm:** Click the **ellipsis (...)** in the top right corner of the Table visual header. Select **Automatically find clusters** .
4. **Verify Output:** Power BI evaluates the inputs and generates a new field (e.g., `StoreName (clusters)`). This field is automatically appended to your Table visual, explicitly categorizing each store into a distinct cluster (e.g., Cluster1, Cluster2) .
5. **Apply as Filter:** This ML-generated field functions identically to standard data. Create a Slicer visual and drag the new cluster field into it to easily isolate performance tiers.
### Exercise 7: Implementing the Key Influencers AI Visual
**Objective:** Deploy the Key Influencers AI visualization to automatically detect underlying data patterns and statistically profile top data segments .
#### Data Input
Save this code block as `Sales_Drivers.csv`.
**Code snippet:**
``` c
TransactionID,TotalSales,Category,Region,CustomerType
1,500000,Audio,North,New
2,1200000,Music, Movies and Audio Books,South,Returning
3,450000,Cameras,East,New
4,1300000,Music, Movies and Audio Books,West,Returning
5,300000,Cell phones,North,Returning
6,1100000,Music, Movies and Audio Books,East,New
```
#### Step-by-Step Instructions
1. **Import Data:** Load `Sales_Drivers.csv` into Power BI Desktop.
2. **Deploy AI Visual:** Switch to the Report view. Select the **Key influencers** visual from the Visualizations pane.
3. **Configure Data Mapping:** Drag `TotalSales` into the **Analyze** field well. Drag `Category` into the **Explain by** field well . (Note: Key influencers require sufficient data variance; experiment with multiple fields if the algorithm returns no results ).
4. **Interpret Key Influencers:** Observe the primary _Key influencers_ tab. The engine calculates and displays the specific category variable (e.g., "Music, Movies and Audio Books") that mathematically drives the highest increase in `TotalSales` .
5. **Profile Data Segments:** Click the **Top segments** tab at the top of the visual . Click on "Segment 1" bubble. Review the generated summary detailing the percentage of data points matching this profile and how far it deviates from the overall average .
6. **Modify Analytical Constraints:** Navigate to **Format visual > Analysis** to configure whether the algorithm treats the targeted data as categorical or absolute .
### Exercise 8: Implementing the Decomposition Tree Visualization
**Objective:** Deconstruct a primary aggregate metric into underlying dimensional components using the Decomposition Tree AI visualization .
#### Data Input
Save this code block as `Product_Decomp.csv`.
**Code snippet:**
``` c
TotalSales,Category,Subcategory
52000,Computers,Desktops
28000,Cell phones,Smartphones
14000,Computers,Laptops
4800,Music, Movies and Audio Books,Audio Books
```
#### Step-by-Step Instructions
1. **Import Data:** Load `Product_Decomp.csv` into Power BI Desktop.
2. **Deploy Visual:** Switch to the Report view. Select the **Decomposition tree** visual from the Visualizations pane.
3. **Map Fields:** Drag `TotalSales` into the **Analyze** field well. Drag `Category` and `Subcategory` into the **Explain by** field well .
4. **Execute Breakdown:** On the visual canvas, click the **+** symbol next to the `TotalSales` root node to expand the analytical hierarchy .
5. **Select Path:** Choose **High value** from the resulting menu. This forces the engine to automatically evaluate all available fields and display the specific dimension driving the highest total .
6. **Isolate Variables:** Click the "Computers" bar in the Category level to explicitly filter the subsequent `Subcategory` path, revealing the exact breakdown for Computers .
7. **Format AI Settings:** Navigate to **Format visual > Analysis**. Toggle **Enable AI splits** to _On_. Adjust the **Density** parameter under **Tree settings** to control the visual compactness of the generated nodes .

**Author:**
Zbigniew Galar