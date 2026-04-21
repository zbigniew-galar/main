# Manage Workspaces in the Service
### Exercise 1: Publishing Artifacts and Navigating the Service
**Objective:** Execute the deployment of a local PBIX file to a centralized cloud workspace and verify the deployment .
#### Prerequisites
A completed report open in Power BI Desktop and active Office 365 credentials.
#### Step-by-Step Instructions
1. **Authenticate:** In Power BI Desktop, click **Sign in** in the upper right-hand corner and input your credentials.
2. **Initiate Publish:** Save the report with a unique name, navigate to the **Home** ribbon, and click **Publish**.
3. **Select Destination:** In the dialogue box, select a designated organizational workspace. Do not select _My workspace_ if the report requires multi-user collaboration . Click **Select**.
4. **Verify Deployment:** Click the immediate success link (e.g., _Open 'filename.pbix' in Power BI_) to instantly launch the web browser and verify the report rendering in the Power BI Service .
### Exercise 2: Establishing Workspace Membership and Governance
**Objective:** Assign explicit access levels to individuals or security groups within a workspace to enforce governance .
#### Step-by-Step Instructions
1. **Access Workspace Settings:** In the Power BI Service, open your target workspace. Locate and click the **Access** tab in the upper menu.
2. **Assign Admin:** Add at least two individuals as Admins to ensure redundancy. Admins possess highest privileges, including workspace deletion .
3. **Assign Members:** Add users who require the ability to add, edit, or delete content, add other users, and publish/update the workspace app .
4. **Assign Contributors:** Add users who strictly require content editing/adding capabilities without administrative overhead. If app updating is required, explicitly grant that optional right.
5. **Assign Viewers:** Add users who solely require read-only access to the workspace content.
### Exercise 3: Authoring Reports Directly in the Service
**Objective:** Construct a new report canvas utilizing an already published dataset without utilizing the Desktop application .
#### Step-by-Step Instructions
1. **Locate Dataset:** Open the target workspace in the Power BI Service. Ensure a published dataset exists.
2. **Initiate Creation:** Click **+ New** in the workspace menu and select **Report** .
3. **Select Data Source:** Choose the existing dataset to bind to the new report canvas.
4. **Build Visuals:** Construct the report using the standard visualizations pane.
    - _Heuristic for Service vs. Desktop Authoring:_ If the data model requires new DAX measures or calculated columns, you must use Power BI Desktop. The Service environment strictly prohibits modifying the underlying data model .
### Exercise 4: Configuring and Deploying an App
**Objective:** Package workspace content into an App for structured organizational distribution and enforce strict permission boundaries .
#### Step-by-Step Instructions
1. **Designate Content:** In the workspace list view, explicitly toggle **Include in app** to _Yes_ for every report and dashboard required in the final package.
2. **Initiate Setup:** Click **Create app** (or **Update app**). Input the mandatory **Description** and optional Support site URL or specific Contact Information .
3. **Configure Navigation:** Switch to the **Navigation** tab. Create Sections (e.g., "Reports", "Dashboards") and drag the designated content into the correct sections to organize the user interface .
4. **Define Audience:** Switch to the **Permissions** tab. Select either _Entire organization_ or _Specific individuals or group_ .
5. **Enforce Constraints:** Uncheck **Build permissions** unless users explicitly require the ability to author new reports against the underlying dataset. Uncheck **Share permissions** unless users are explicitly authorized to distribute the app further .
6. **Deploy:** Publish or Update the app.
### Exercise 5: Applying Endorsement Tags
**Objective:** Execute content promotion to visually signal data reliability and quality to downstream consumers .
#### Step-by-Step Instructions
1. **Select Artifact:** In the workspace, locate a verified Report, Dataset, Dataflow, or App .
2. **Access Settings:** Click the **Ellipsis (...)** next to the artifact and open its Settings.
3. **Apply Promotion:** Locate the Endorsement section and select **Promoted**. (Note: The _Certified_ tag requires specific administrative enablement and adherence to internal organizational governance policies; it cannot be applied arbitrarily by standard users ).

**Author:**
Zbigniew Galar