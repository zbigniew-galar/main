# Power BI UX Optimization
### Exercise 1: Filter Optimization and Engine Load Reduction
**Objective:** Minimize analytical engine query execution costs caused by filter interactions.
#### Data Input
Save this code block as `High_Volume_Transactions.csv`.
**Code snippet:**
``` c
TransactionID,Region,Status,Amount
1,North,Completed,500
2,South,Pending,300
3,East,Completed,800
4,West,Failed,150
```
#### Step-by-Step Instructions
1. **Import Data:** Load `High_Volume_Transactions.csv` into Power BI Desktop.
2. **Observe Query Cost:** Every interaction within the filter pane generates a distinct query to the analytical engine.
3. **Apply Optimization Heuristics:**
    - **Variable: Unnecessary data loading.** _Action:_ Apply preliminary selections at the Power Query level to prevent loading unused high-cardinality data.
    - **Variable: Overabundant visual slicers.** _Action:_ Consolidate slicers into the core filter pane to reduce canvas rendering times and standardize visual consistency.
### Exercise 2: Architectural Routing (Interactive vs. Paginated)
**Objective:** Define the correct deployment architecture strictly based on the required output format.
#### Implementation Heuristic
- **Variable:** The deliverable requires exact physical dimensions (pixel-perfect), company letterhead integration, or rendering every single row of a massive dataset (e.g., a 50-page inventory table) without scrollbars.
    - **Action:** Build a Paginated Report using **Power BI Report Builder**. Standard dashboards will fail this requirement.
- **Variable:** The deliverable requires on-screen data exploration, cross-filtering, and trend analysis within a constrained digital canvas.
    - **Action:** Build an Interactive Report using **Power BI Desktop**.
### Exercise 3: Constructing Drill-Through Navigation Paths
**Objective:** Guide users through multi-level analytical paths using Drill-through filters and buttons to reduce cognitive friction.
#### Data Input
Use the `High_Volume_Transactions.csv` data from Exercise 1.
#### Step-by-Step Instructions
1. **Establish Destination:** Rename Page 1 to `Summary` and create Page 2 named `Region Details`.
2. **Configure Drill-Through:** On the `Region Details` page, locate the **Add drill-through fields here** well in the Visualizations pane. Drag the `Region` field into this well.
3. **Implement Button Routing:** Return to the `Summary` page. Create a Bar Chart displaying `Amount` by `Region`. Add a blank Button visual to the canvas.
4. **Configure Button Action:** Select the button. In the Format pane, enable **Action**. Set the **Type** to _Drill through_ and the **Destination** to _Region Details_.
5. **Execute Navigation:** Select the "North" bar in the chart. The button becomes active. Ctrl+click the button to instantly navigate to the `Region Details` page, automatically filtered to the North region.
### Exercise 4: Dynamic Visual Adaptation via DAX Titles
**Objective:** Automate visual context updates using conditional formatting and DAX expression titles.
#### Data Input
Use the `High_Volume_Transactions.csv` data from Exercise 1.
#### Step-by-Step Instructions
1. **Author DAX Expression:** Create a new measure to dynamically read the filter context:
    `Dynamic Region Title = "Transaction Volume for " & SELECTEDVALUE(High_Volume_Transactions[Region], "All Regions")`.
2. **Construct Visual:** Add a Card visual displaying the sum of `Amount`. Add a Slicer for `Region`.
3. **Inject Dynamic Title:** Select the Card visual. Navigate to **Format visual > General > Title**. Toggle the Title to _On_.
4. **Apply Conditional Formatting:** Click the **fx** (Conditional formatting) icon next to the Title text box.
5. **Map to Measure:** In the dialog, set **Format style** to _Field value_. Select the `Dynamic Region Title` measure and click **OK**.
6. **Verify Adaptation:** Click different regions in the slicer. The Card visual's title instantly adapts to match the specific data context.

**Author:**
Zbigniew Galar