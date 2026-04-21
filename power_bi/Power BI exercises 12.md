# Create Dashboards
### Exercise 1: Constructing a Baseline Dashboard
**Objective:** Extract individual visualizations from existing reports to construct a consolidated, single-page dashboard .
#### Step-by-Step Instructions
1. **Access Source Report:** Open a published report within the Power BI Service.
2. **Execute Pin Action:** Hover over a target visualization. Click the **Pin icon** (pushpin) located in the visual's header .
3. **Define Destination:** In the dialog box, select **New dashboard** to initialize a new container, or **Existing dashboard** to append it to an active layout .
4. **Navigate to Dashboard:** Click **Go to dashboard** on the temporary pop-up notification, or use the left-hand navigation pane to locate the newly created dashboard .
### Exercise 2: Integrating Static Media and Streaming Data
**Objective:** Augment the dashboard with non-report elements, such as text boxes, images, or real-time streaming data feeds .
#### Step-by-Step Instructions
1. **Initiate Tile Addition:** On the active dashboard, click **Edit** in the top menu ribbon, then select **Add a tile** .
2. **Select Media Type:** In the Add a tile dialogue box, choose the desired source category: _Web content_, _Image_, _Text box_, _Video_, or _Custom Streaming Data_ .
3. **Configure Source:** Input the required parameters (e.g., URL for an image/video, or text for a text box). Click **Apply** to render the custom tile on the dashboard canvas.
### Exercise 3: Extracting Tile Data and Generating AI Insights
**Objective:** Export the underlying data of a specific dashboard tile to a CSV file and execute the AI engine to automatically detect data patterns .
#### Step-by-Step Instructions
1. **Export Data:** Hover over a specific tile on the dashboard. Click the **Ellipsis (...)** in the upper right corner. Select **Export to .csv** to download the raw data populating that exact visual .
2. **Trigger AI Analysis:** Click the **Ellipsis (...)** on the tile again. Select **View insights**.
3. **Review and Pin Insights:** The Power BI AI engine will evaluate the tile's data and generate new visual representations of detected patterns. If an insight is valuable, click its **Pin icon** to permanently add it to the dashboard .
### Exercise 4: Pinning Live Report Pages
**Objective:** Bypass default static tile behavior by pinning an entire report page to the dashboard, retaining full cross-filtering interactivity .
#### Step-by-Step Instructions
1. **Access Report Page:** Open a published report in the Service and navigate to the target page. Ensure you are in _Read mode_ .
2. **Execute Page Pin:** Click the **Ellipsis (...)** in the top report menu. Select **Pin to a dashboard**.
3. **Verify Interactivity:** Navigate to the destination dashboard. The pinned page functions as a single, large tile. Unlike standard tiles, selecting elements within this live page will dynamically cross-filter the other elements within that specific tile boundary . The source report name and page number will permanently display in its upper left corner.
### Exercise 5: Executing Natural Language Queries (Q&A)
**Objective:** Configure the Q&A engine and query the underlying dataset using natural language to automatically generate new visual tiles .
#### Step-by-Step Instructions
1. **Enable Desktop Configuration:** Open the source file in Power BI Desktop. Navigate to the **Modeling** ribbon and click **Q&A setup**. Publish the report.
2. **Enable Service Configuration:** In the Power BI Service workspace, click the **Ellipsis (...)** next to the Dataset. Select **Settings**. Expand the **Q&A** section and check the box to turn on natural language questions.
3. **Execute Query:** Open the dashboard connected to this dataset. Click into the **Ask a question about your data** field at the top of the canvas.
4. **Generate Visual:** Type a natural language query (e.g., "what is the most recent order"). The engine will automatically generate a visual answering the query.
5. **Pin Output:** Click **Pin visual** in the upper right corner of the Q&A interface to save the newly generated chart to the dashboard.
### Exercise 6: Mobile Layout Configuration and Dashboard Management
**Objective:** Optimize the dashboard for mobile consumption, apply global aesthetic themes, and execute manual visual refreshes .
#### Step-by-Step Instructions
1. **Apply Global Theme:** Open the active dashboard. Click **Edit > Dashboard theme**. Change the theme to _Dark_ or _Color-blind friendly_ to alter the entire canvas simultaneously, or upload a custom JSON theme file .
2. **Access Dashboard Settings:** Navigate to **File > Settings** to expose the management controls .
3. **Configure Tile Flow:** In the Settings menu, locate **Dashboard tile flow**. Toggle this to _On_ to force Power BI to automatically rearrange and compact tiles when items are added or deleted .
4. **Initiate Mobile Layout:** Click **Edit > Mobile layout** in the top ribbon .
5. **Optimize for Mobile:** The canvas shifts to a smartphone proportion. Unpin non-essential tiles from this specific view to reduce clutter, and drag the remaining tiles to arrange them logically. This modification strictly affects the mobile view, leaving the desktop layout intact .
6. **Execute Manual Refresh:** Switch back to the standard web layout. Click the **Refresh icon** (circular arrow) in the upper right-hand corner of the dashboard to force the tiles to immediately query and display the latest data from their underlying scheduled datasets .

**Author:**
Zbigniew Galar