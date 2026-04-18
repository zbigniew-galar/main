# Prepare the Data
### Exercise 1: Data Extraction and File Path Parameters
**Objective:** Import data using the Power Query Editor and create a parameter to easily switch the data source file path, a common and practical use case for parameters.
#### Data Input
Please save the following two code blocks as separate CSV files on your computer. Note the exact file paths where you save them (e.g., `C:\SampleData\RegionA_Sales.csv` and `C:\SampleData\RegionB_Sales.csv`).
**File 1: RegionA_Sales.csv**
``` c
Date,Region,Product,Revenue
2023-10-01,Region A,Widget A,150.00
2023-10-02,Region A,Widget B,200.50
2023-10-03,Region A,Widget C,120.00
```
**File 2: RegionB_Sales.csv**
``` c
Date,Region,Product,Revenue
2023-10-01,Region B,Widget A,300.00
2023-10-02,Region B,Widget B,150.75
2023-10-03,Region B,Widget C,400.00
```
#### Step-by-Step Instructions
1. **Initiate Data Extraction:**
    - Open Power BI Desktop.
    - On the **Home** tab, click **Get data** and select **Text/CSV**.
    - Navigate to where you saved `RegionA_Sales.csv`, select it, and click Open.
2. **The Navigator Window:**
    - When the Navigator dialogue box appears, do not choose the **Load** button, even if the data looks clean.
    - Choose **Transform Data** to open the Power Query Editor.
3. **Define a New Parameter:**
    - In the Power Query Editor, go to the **Home** tab and select **Manage Parameters**, then click **New Parameter**.
    - Name the parameter `FilePath` and add a description like "Enable users to change the file path easily".
    - Set the **Type** to `Text`.
4. **Populate the Parameter List:**
    - For **Suggested Values**, select `List of values`.
    - In the list that appears, enter the exact file path for `RegionA_Sales.csv` in row 1, and the exact file path for `RegionB_Sales.csv` in row 2.
    - Set the **Default Value** and **Current Value** to your Region A file path. Click **OK**.
5. **Apply the Parameter to Your Query:**
    - Select your `RegionA_Sales` query on the left pane.
    - In the **Applied Steps** pane on the right, click the gear icon next to the **Source** step.
    - In the dialogue box, change the file path input from a hardcoded string to your new `FilePath` parameter.
6. **Test the Parameter:**
    - On the left Queries pane, click on your `FilePath` parameter.
    - Change the **Current Value** from the Region A path to the Region B path using the dropdown.
    - Click back on your `RegionA_Sales` query; you should now see the data for Region B populated in the preview.
7. **Enable Load for the Desktop (Optional):**
    - If you want to allow users to change this parameter directly from the Power BI Desktop (outside of the Power Query Editor), right-click the `FilePath` parameter in the Queries pane and select **Enable load**.
    - Once you choose **Close & Apply**, you can access this parameter on the front end by navigating to **Transform data > Edit parameters**.
### Exercise 2: Connect to a Folder and Combine Files
**Objective:** Learn how to connect to a local folder and append multiple files together automatically using the "Combine & Transform Data" feature.
#### Data Input
Create a new folder on your computer and name it `Monthly_Sales_Data`. Save the following two code blocks as separate CSV files directly inside this new folder. It is important that these files have the exact same column structure.
**File 1: 2023_Jan_Sales.csv**
``` c
Date,Product,Units,Revenue
2023-01-15,Widget A,10,150.00
2023-01-20,Widget B,5,100.25
2023-01-28,Widget C,12,144.00
```
**File 2: 2023_Feb_Sales.csv**
``` c
Date,Product,Units,Revenue
2023-02-10,Widget A,15,225.00
2023-02-18,Widget B,8,160.40
2023-02-25,Widget C,20,240.00
```
#### Step-by-Step Instructions
1. **Initiate Folder Connection:**
    - Open Power BI Desktop (or open a new PBIX file).
    - On the **Home** tab, click **Get data** and select **More...** to view all available connectors.
    - In the Get Data dialogue box, select **Folder** and click **Connect**.
2. **Locate the Folder:**
    - Click **Browse...** and navigate to the `Monthly_Sales_Data` folder you created earlier.
    - Select the folder and click **OK**, then click **OK** again.
3. **Review Folder Metadata:**
    - You will see a preview window displaying the metadata of the folder (a list of the files it contains), such as Content, Name, Extension, Date accessed, and Date modified.
4. **Combine and Transform:**
    - At the bottom of this dialogue box, instead of choosing "Transform Data" to just bring in the file names, select the dropdown next to "Combine" and choose **Combine & Transform Data**.
5. **Evaluate the Combine Files Window:**
    - Power BI will evaluate the files. In the "Combine Files" dialogue box, ensure the "Sample File" is set to the first file (or a specific file of your choosing) so Power BI knows which structure to use as the template.
    - Click **OK**.
6. **Review in Power Query Editor:**
    - The Power Query Editor will open. On the left Queries pane, you will see a new helper folder created by Power BI, along with your final combined query (likely named `Monthly_Sales_Data`).
    - Look at the main data preview. Notice that Power BI has automatically appended the rows from the February file underneath the rows from the January file.
    - You will also see a new `Source.Name` column that identifies which file each row of data originated from.
### Exercise 3: Resolving a Broken Data Source Connection
**Objective:** Understand how Power BI retains file path metadata and learn how to resolve data extraction errors when a source file is moved or renamed, which is one of the most common errors encountered in Power Query.
#### Data Input
Please save the following code block as a CSV file named `Employee_Directory_v1.csv` in a folder on your computer (for example, your Documents folder).
``` c
EmployeeID,Name,Department,Role
1001,Jane Doe,Finance,Analyst
1002,John Smith,IT,Developer
1003,Alice Jones,HR,Manager
```
#### Step-by-Step Instructions
1. **Initial Data Extraction:**
    - Open Power BI Desktop and start a new file.
    - On the **Home** tab, choose **Get data > Text/CSV** and connect to `Employee_Directory_v1.csv`.
    - In the Navigator dialogue box, choose **Load** (since this data is clean and ready).
    - Save your Power BI Desktop file as `HR_Report.pbix` and close Power BI Desktop completely.
2. **Simulate a Moved Data Source:**
    - Open your computer's File Explorer.
    - Locate `Employee_Directory_v1.csv` and rename it to `Employee_Directory_FINAL.csv`. (Alternatively, move it to a completely different folder).
    - _Concept Check:_ The Power BI query retains the metadata of the original file path. Because the file no longer exists at that exact path with that exact name, the path will not resolve.
3. **Trigger the Error:**
    - Reopen your `HR_Report.pbix` file.
    - On the **Home** tab, click **Refresh**.
    - You will see an error pop up stating that Power BI could not find a part of the path.
4. **Access Data Source Settings:**
    - On the **Home** tab, click **Transform data** to open the Power Query Editor.
    - You will see a yellow warning banner stating `DataSource.Error: Could not find a part of the path...`.
    - To fix this, navigate to the **Home** tab within the Power Query Editor and click **Data source settings**.
5. **Change the Source:**
    - In the Data source settings dialogue box, you will see the broken file path listed under "Data sources in current file".
    - Select the file path and click the **Change Source...** button at the bottom.
6. **Browse for the New File:**
    - In the next dialogue box, click **Browse...** next to the File path.
    - Navigate to your newly renamed file (`Employee_Directory_FINAL.csv`), select it, and click **Open**.
    - Click **OK**, then click **Close** on the Data source settings window.
7. **Verify the Fix:**
    - The yellow error banner should disappear, and the Power Query Editor will display your data preview again.
    - Click **Close & Apply** to finalize the updated connection string.
