# Enhance Reports
### Exercise 1: Custom Sort Orders via Index Columns
**Objective:** Override native alphabetical text sorting by explicitly mapping a text column to a numerical index column .
#### Data Input
Save this code block as `Calendar_Sort.csv`.
**Code snippet:**
``` c
Date,MonthName,MonthNum,Sales
2023-01-01,Jan,1,500
2023-02-01,Feb,2,600
2023-03-01,Mar,3,750
2023-04-01,Apr,4,400
```
#### Step-by-Step Instructions
1. **Import Data:** Load `Calendar_Sort.csv` into Power BI Desktop.
2. **Select Target Column:** Switch to Data view. Select the `MonthName` column.
3. **Apply Sort Logic:** On the **Column tools** ribbon, click **Sort by column** and select `MonthNum`.
4. **Verify Sort:** Switch to Report view. Create a Table visual with `MonthName` and `Sales`. The table will correctly sort chronologically (Jan, Feb, Mar) instead of alphabetically (Apr, Feb, Jan).
### Exercise 2: Executing Hierarchical Navigation Controls
**Objective:** Navigate multi-layered hierarchical structures within matrix visuals using explicit drill-down and expand controls .
#### Data Input
Save this code block as `Product_Hierarchy.csv`.
**Code snippet:**
``` c
Category,Subcategory,Product,Sales
Technology,Computers,Laptop A,1500
Technology,Computers,Desktop B,1200
Technology,Audio,Headphones,200
Furniture,Seating,Desk Chair,300
```
#### Step-by-Step Instructions
1. **Import Data:** Load `Product_Hierarchy.csv`.
2. **Build Hierarchy:** In the Report view, create a Matrix visual. Drag `Category`, `Subcategory`, and `Product` into the **Rows** well in that exact order . Drag `Sales` into the **Values** well.
3. **Drill Down:** Click the **Drill down icon** (single downward arrow) in the visual header to turn it on (it will highlight black). Click the "Technology" row to filter the entire visual down to the Subcategory level for Technology only.
4. **Drill Up:** Click the **Up arrow** to return to the top Category level .
5. **Expand Next Level:** Click the **Double arrows** to display the Subcategory level for all categories simultaneously, without displaying the parent Category names . Click the Up arrow to return.
6. **Expand All Down:** Click the **Trident icon** (split downward arrow) to expose the Subcategory level while retaining the parent Category names in the visual .
### Exercise 3: Modifying Cross-Visual Interactions
**Objective:** Override default cross-highlighting behavior to enforce strict filtering or total visual isolation .
#### Data Input
Use the `Product_Hierarchy.csv` data from Exercise 2.
#### Step-by-Step Instructions
1. **Construct Visuals:** Create a Pie Chart displaying `Sales` by `Category`. Create a Bar Chart displaying `Sales` by `Subcategory`.
2. **Observe Default:** Click "Technology" in the Pie Chart. The Bar Chart highlights the Technology subcategories by graying out the Furniture subcategories .
3. **Enable Edit Mode:** Select the Pie Chart. Navigate to **Format > Edit interactions** .
4. **Apply Filter Interaction:** Locate the interaction icons now visible at the top right of the Bar Chart. Click the **Filter icon** (leftmost icon) . Click "Furniture" in the Pie Chart; the Bar Chart now explicitly filters out Technology entirely rather than graying it out.
5. **Apply None Interaction:** Click the **None icon** (circle with a line) on the Bar Chart. Clicks on the Pie Chart will no longer impact the Bar Chart.
### Exercise 4: Capturing States via Bookmarks and the Selection Pane
**Objective:** Isolate visual elements using groups, dictate visibility via the Selection pane, and capture these specific structural states using Bookmarks .
#### Data Input
Use `Product_Hierarchy.csv`.
#### Step-by-Step Instructions
1. **Setup Canvas:** Create a Slicer for `Category`. Create a Table for `Product` and `Sales`. Add a blank Button visual to the canvas.
2. **Access Panes:** Navigate to the **View** ribbon. Enable both the **Bookmarks** and **Selection** panes .
3. **Group Elements:** In the Selection pane, hold Ctrl and click the Table and the Button. Right-click and select **Group** . Rename the group to `Details Group` .
4. **Capture Default State:** In the Bookmarks pane, click **Add**. Rename it `Default View` .
5. **Modify Visibility:** In the Selection pane, click the **Eye icon** next to `Details Group` to hide it (a slash will appear) .
6. **Capture Hidden State:** In the Bookmarks pane, click **Add**. Rename it `Hidden Details`.
7. **Test Navigation:** Click between the `Default View` and `Hidden Details` bookmarks in the pane to observe the elements appearing and disappearing based on the captured Display properties .
### Exercise 5: Constructing Report Page Tooltips
**Objective:** Replace default black-box tooltips with an embedded, dynamically filtered report canvas .
#### Data Input
Use `Product_Hierarchy.csv`.
#### Step-by-Step Instructions
1. **Create Tooltip Page:** Click the **+** icon at the bottom of the workspace to add a new page. Right-click the page tab and select **Hide Page** .
2. **Configure Canvas:** With no visuals selected, navigate to **Format page > Page information**. Toggle **Allow use as tooltip** to _On_ .
3. **Set Dimensions:** Under **Canvas settings**, change the Type to _Tooltip_ to automatically resize the canvas to standard tooltip dimensions .
4. **Build Embedded Visual:** Add a Card visual to this small canvas displaying the `Sales` field.
5. **Link Tooltip:** Return to Page 1. Create a Bar Chart displaying `Sales` by `Product`.
6. **Apply Configuration:** Select the Bar Chart. Navigate to **Format visual > General > Tooltips**. Ensure Tooltips are _On_. Set the **Type** to _Report page_ and set the **Page** dropdown to your hidden tooltip page name .
7. **Verify Execution:** Hover over any bar in the Bar Chart. The embedded Card visual will appear and dynamically filter to display the exact sales value for the specific product hovered over .
### Exercise 6: Designing for Mobility
**Objective:** Construct a dedicated layout optimized for smartphone and tablet viewing without altering the core desktop report configuration .
#### Data Input
Use `Product_Hierarchy.csv` from the previous exercises. Ensure at least one slicer and two standard visuals exist on the desktop canvas.
#### Step-by-Step Instructions
1. **Initiate Mobile Canvas:** Navigate to the **View** ribbon. In the Page view section, click **Mobile layout**. The central canvas transforms into a vertical smartphone template.
2. **Populate Layout:** Locate the **Page visuals** pane on the right, which lists all elements currently existing on the desktop page. Drag the existing slicer and charts from this pane directly onto the mobile canvas.
3. **Arrange and Align:** Position the slicer at the top of the canvas for immediate access. Use the background grid to snap the charts into place beneath it. Power BI auto-adjusts elements to fit the device bounds.
4. **Optimize Formatting:** Select a visual on the mobile canvas. Open the **Visualizations** pane and adjust settings (e.g., axis text size, legend position) to maximize small-screen readability.
5. **Verify Independence:** Click **Mobile layout** again to toggle back to the standard desktop view. Confirm that the desktop layout remains strictly unaltered by the mobile optimizations.

**Author:**
Zbigniew Galar