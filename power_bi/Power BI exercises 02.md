# Clean and Transform the Data basics
### Exercise 1: Splitting Columns and Replacing Values
**Objective:** Practice foundational data shaping techniques, including accessing the Power Query Editor, splitting columns, renaming applied steps, and properly handling null values.
#### Data Input
Save the following data block as a CSV file named `Quality_Control_Log.csv` on your local machine.
**Code snippet:**
``` c
LogID,CommentText,InspectionDate,Cost
1,QUAL 99919, WIRED WRONG @ PLUG,01/15/2023,150.50
2,QUAL 99886, TO SHORT,01/16/2023,
3,QUAL 99916, BROKEN TERMINAL,01/17/2023,null
4,QUAL 99806, MISSING THERMISTOR,01/18/2023,45.00
```
#### Step-by-Step Instructions
1. **Access the Power Query Editor:** Open Power BI Desktop and initiate data extraction by choosing **Get data > Text/CSV** to load your saved file. Instead of loading the data directly, choose **Transform data** to open the Power Query Editor in a separate window.
2. **Split the Column:** Select the `CommentText` column. Right-click the column header and choose **Split Column > By Delimiter...**. Ensure the delimiter is set to a comma and execute the split to separate the QUAL code from the comment text.
3. **Rename the Step:** In the **Applied Steps** pane on the right, locate the new step created for the split. Right-click this step and choose **Rename** to give it a descriptive name like "Split Comment by Comma".
4. **Document the Step:** Right-click your newly renamed step and choose **Properties**. Enter a description of what you did and why, then click OK to see the small "i" icon appear next to the step.
5. **Replace Null Values:** Select the `Cost` column. Right-click the column and choose **Replace Values**. The Power Query Editor treats Null and Blank values differently. To specifically target the null value, enter `null` in the "Value To Find" box, and enter `0` in the "Replace With" box.
6. **Apply Changes:** Click **Close & Apply** on the Home tab to finalize your transformations and load the cleaned data into the Power BI Desktop data model.
### Exercise 2: Data Profiling, Cardinality, and Locales
**Objective:** Assess data quality using profiling tools to determine cardinality, identify key columns , and properly assign data types using Locales for international formatting .
#### Data Input
Save the following data block as a CSV file named `International_Sales.csv` on your local machine. Notice the dates use a DD/MM/YYYY format.
**Code snippet:**
``` c
CustomerID,Region,OrderDate,Revenue
CUST-101,EMEA,31/10/2023,1500.50
CUST-102,EMEA,15/11/2023,200.00
CUST-103,APAC,28/11/2023,3450.75
CUST-104,APAC,05/12/2023,99.99
CUST-105,LATAM,12/12/2023,500.00
```
#### Step-by-Step Instructions
1. **Load and Transform:** Extract `International_Sales.csv` into Power BI Desktop and choose **Transform data** to open the Power Query Editor.
2. **Enable Data Preview Tools:** Navigate to the **View** tab. Check the boxes for **Column quality**, **Column distribution**, and **Column profile** .
3. **Assess High Cardinality (Keys):** Select the `CustomerID` column and look at the profiling metrics. Observe the ratio of distinct to unique values. A $1/1$ ratio means every value is unique, indicating high cardinality. This confirms the column serves as the unique identifier, or "key", for this table.
4. **Assess Low Cardinality:** Select the `Region` column. Observe that the number of unique values is lower than the distinct values, indicating values are repeated and the column has low cardinality .
5. **Convert Data Type Using Locale:** Select the `OrderDate` column. Because the dates are formatted as Day/Month/Year, a standard Date conversion might fail depending on your system settings. Click the data type icon (ABC/123) in the column header and select **Using Locale...**.
6. **Configure the Locale:** In the dialogue box, set the Data Type to **Date** and set the Locale to **English (United Kingdom)** (or another locale that uses DD/MM/YYYY). Click OK. This feature automatically translates the regional format into a standard date recognized by Power BI .
7. **Set Currency Data Type:** Select the `Revenue` column. Click the data type icon and change it to **Fixed decimal number**. Currency should always be stored as a Fixed Decimal type.
8. **Disable Profiling:** Return to the **View** tab and uncheck the Data Preview tools to reclaim screen real estate . (Simplified profiling will remain visible via the green peek bar ).
### Exercise 3: Diagnosing and Resolving Data Errors
**Objective:** Isolate cell-level errors by adjusting data profiling behavior and utilizing the Keep Errors functionality.
#### Data Input
Save the following block as a CSV file named `Vendor_Transactions.csv`. The text values in numeric and date columns will trigger type conversion errors in Power Query.
**Code snippet:**
``` c
TransactionID,Vendor,Quantity,TransDate
1,Lexiqvolax,50,2019-09-16
2,Massive Dynamic,100,2019-09-17
3,Hottechi,N/A,2019-09-18
4,Newex,75,Pending
```
#### Step-by-Step Instructions
1. **Import and Transform:** Extract `Vendor_Transactions.csv` into Power BI Desktop and select **Transform data**. Power Query will automatically apply a "Changed Type" step, causing the "N/A" and "Pending" values to generate errors.
2. **Adjust Profiling Behavior:** Look at the status bar in the lower-left corner of the Power Query Editor window. Click the text that says **Column profiling based on top 1000 rows** and change it to **Column profiling based on entire data set** . This ensures all errors are detected in large datasets .
3. **Diagnose the Error:** Click into the empty whitespace of a cell displaying the word _Error_ in the `Quantity` column. The error message, such as `DataFormat.Error: Invalid cell value`, will appear in a yellow band at the bottom of the screen . Do not click the hyperlinked word _Error_, as this adds an unnecessary navigation step.
4. **Isolate Error Rows:** Right-click the Data Quality peek bar (the colored line directly under the `Quantity` column header) to open the error-specific contextual menu. Select **Keep Errors** . A new applied step named "Kept Errors" is created, and the query now exclusively displays the problematic rows .
5. **Clear Isolation:** Delete the "Kept Errors" step from the Applied Steps pane by clicking the red **X** next to it .
6. **Replace Errors:** Right-click the `Quantity` column header and select **Replace Errors** . Enter `0` in the dialogue box and click **OK**. Repeat this process for the `TransDate` column, replacing the error with a null or default date value.

**Author:**
Zbigniew Galar
