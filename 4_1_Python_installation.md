### Basic Python installation set up
Install Python from: https://www.python.org/downloads/release/python-3113/

Install VS Code from: https://code.visualstudio.com/

Create folders for your code and data files in your main drive for example:
**Files storage example folder:**
C://Python repositories//Education project//src//code
**Data storage example folder:**
C://Python repositories//Education project//src//data

Lunch MS Visual Studio Code.

In "Extensions" install Python.

**Choose working directory:**
File -> Open Folder -> C://Python repositories//Education project.

**To store Python abilities for our project like we create a "venv" subfolder via PowerShell terminal:**
``` powershell
# Creating and activating environment
>>> py -m venv venv
>>> venv\Scripts\activate.bat
# Troubleshooting
>>> .\venv\Scripts\Activate.ps1
>>> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```
**For Mac:**
``` powershell
>>> python3 -m venv /Users/User_name/venv1
>>> source venv1/bin/activate
```
**Upgrading libraries installation engine and installing libraries:**
``` powershell
# Upgrading
(venv) PS C:\Python repositories\Education project>python.exe -m pip install --upgrade pip
```
**Install data processing capabilities:**
``` powershell
(venv) PS C:\Python repositories\Education project>pip install pandas
```
**Install Excel processing capabilities:**
``` powershell
(venv) PS C:\Python repositories\Education project>pip install xlsxwriter
```
**or alternative Excel processing capabilities:**
``` powershell
(venv) PS C:\Python repositories\Education project>pip install openpyxl
```
**For Mac:**
``` powershell
python3 -m pip install pandas
```
**Check the python version:**
``` powershell
py 3 --version
```
**For Mac:**
``` powershell
python3 --version
```
