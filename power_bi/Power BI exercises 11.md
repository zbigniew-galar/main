# Deploy and Maintain Assets
### Exercise 1: Configuring Automated Dataset Refreshes
**Objective:** Schedule automatic data updates and establish failure notification routing to maintain data currency .
#### Prerequisites
A published Power BI dataset and a Pro or Premium license .
#### Step-by-Step Instructions
1. **Access Settings:** In the Power BI Service workspace, locate the target dataset. Click the **Ellipsis (...)** next to the dataset and select **Settings** .
2. **Enable Refresh:** Expand the **Scheduled refresh** section. Toggle the switch to **On**.
3. **Configure Cadence:** Select the **Refresh frequency** (e.g., Daily) and define the specific **Time zone** .
4. **Set Execution Times:** Click **Add another time** to specify exact execution times. The Service may execute the refresh slightly before or after the designated minute .
5. **Define Failure Routing:** In the **Send refresh failure notifications to** section, check **Dataset owner** and specify additional critical contacts. Three consecutive failures will permanently disable the schedule . Click **Apply**.
### Exercise 2: Mapping Row-Level Security (RLS) Roles
**Objective:** Assign specific Azure Active Directory users or security groups to the DAX-defined security roles authored in Power BI Desktop .
#### Step-by-Step Instructions
1. **Access Security Manager:** In the workspace, click the **Ellipsis (...)** next to the dataset. Select **Security** .
2. **Select Role:** The Row-Level Security page displays all roles packaged within the published PBIX file. Select the target role on the left pane.
3. **Assign Members:** In the **Members** well on the right, enter the email addresses or security group names of the authorized personnel.
4. **Save Configuration:** Add the users and explicitly save the configuration to activate the data filtering for those credentials.
### Exercise 3: Granting Direct Build and Share Permissions
**Objective:** Authorize specific users to construct new reports connected to a dataset or reshare the dataset without elevating them to workspace Admins, Members, or Contributors .
#### Step-by-Step Instructions
1. **Access Permission Manager:** Click the **Ellipsis (...)** next to the dataset and select **Manage permissions** .
2. **Initiate Direct Access:** In the Permissions dialogue box, select the **Direct access** tab, then click **+ Add user**.
3. **Define Recipient:** Enter the name or email address of the target individual.
4. **Declare Permissions:** Check **Allow recipients to build content with the data associated with this dataset** to grant Build rights. Check **Allow recipients to share this dataset** to grant Share rights.
5. **Execute:** Click **Grant access**.
### Exercise 4: Generating Permission-Bound Sharing Links
**Objective:** Distribute report access via a URL that intrinsically contains defined read, share, and build permissions.
#### Step-by-Step Instructions
1. **Target Report Level:** Link generation requires selecting the report artifact, strictly _not_ the dataset.
2. **Initiate Link Creation:** Open the report or click the Share icon next to the report name. Select **Add link** .
3. **Define Link Scope:** Click the settings gear or the current scope description (e.g., "People in your organization") to modify who can utilize the link.
4. **Embed Permissions:** Under the Settings section of the link configuration, check or uncheck **Allow recipients to share this report** and **Allow recipients to build content...** to strictly govern downstream data usage.
5. **Generate and Distribute:** Click **Apply**. Copy the generated URL to distribute to the authorized audience. Manage or revoke this specific link later via the **Links** tab within the Manage permissions menu.

**Author:**
Zbigniew Galar