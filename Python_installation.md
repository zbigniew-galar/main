### Python installation
Install Python downloader from:
https://www.python.org/downloads/release/python-3113/

Use admin privileges when installing for all users.

So that you can run python and pip commands from any command prompt or terminal without specifying the full path to the Python executable.
Select "Add python.exe to PATH".
	**To add path manually:**
``` 
setx path "%PATH%;C:\Users\HP\AppData\Local\Programs\Python\Python311\Scripts;"
```
Install [[MS Visual Studio Code]] from:
https://code.visualstudio.com/

Create a working directory on the drive.

Lunch [[MS Visual Studio Code]].

In "Extensions" install Python.

Choose the code interpreter:
   - Show all commands: Ctrl + Shift + P
   - Python: Select Interpreter -> (Choose from the list)

Choose working directory:
File -> Open Folder -> (Choose the project folder).

Create the virtual environment. First start "Command prompt" terminal in the project folder:
```
# Environment creation with name: "venv"
py -m venv venv
# Activation
venv\Scripts\activate.bat
# or
call venv\Scripts\activate
```
For Mac:
```
python3 -m venv /Users/User_name/venv1
source venv1/bin/activate
```
To install new libraries we start the PowerShell on Windows or zsh on Mac terminal:
```
# Checking if we have the latest version of software that install new libraries:
py -m pip install --upgrade pip
# Libraries to install
pip install numpy
pip install pandas
pip install openpyxl 
pip install sql
```
For Mac:
```
python3 -m pip install numpy
```
Check the python version:
```
py 3 --version
```
For Mac:
```
python3 --version
```
To execute commands directly in Pyhon:
```
py
quit()
```
To execute modules directly:
```
py main.py
```
For Mac:
```
python3 main.py
```
To start REPL which stands for Read-Eval-Print Loop and run Python directly without any files open a terminal or command prompt and type:
``` console
python
>>> 
```
Clear terminal (console):
``` console
> clear
```
Code can be executed directly in terminal as script files:
``` console
> python main.py
```
Or it can be executed as a module when imported to another py file:
``` python
import my_module
```
When a py file contains a definition of a function that can be used elsewhere a separation of definitions of functions and classes from the executable code is useful. Test code can be executed only when script file is started directly. 
To avoid execution of the code when imported as module we use (part that follows will execute only when py file is executed directly):
``` python
if __name__ == "__main__":
```
Stating path to the interpreter used to run the script example (this is not obligatory):
``` python
#!/usr/bin/python3
```
Default code indentation should be 4 spaces:
``` python
def main():
    print("Print")
```
Check basic venv settings in powershell console:
```
python --version
pip --version
pip list
```
Display basic version control information:
``` python
import sys
print(sys.version)
print() # adds a space between outputs
print(sys.winver)
print(sys.gettrace)
print(sys.argv)
```
Get help on specific module:
``` python
import pandas as pd
help(pd)
```
### VS Code installation
**Select: "Add to PATH (requires shell restart)"**
PATH is an environment variable in operating systems like Windows. PATH specifically is a list of directories (folders) where the system looks for executable files (programs or commands) when you type a command in a terminal. 
PATH is a string of directory paths separated by semicolons (on Windows). 
When you open a Command Prompt and type a command like code the OS doesn't know where to find the code.exe executable file by default. Instead, it searches through the directories listed in the PATH variable in sequence until it finds a matching executable. Without it, you'd have to type the full path to an executable every time:
``` python
C:\Users\YourName\AppData\Local\Programs\Microsoft VS Code\bin\code.exe
# vs
code
```
### Setting up a new project in VS Code
1. Create new folder under C:/Python repositories.
2. Open MS Visual Studio Code.
3. File -> Open folder.
4. Select: "Trust the authors of all files in the parent folder...".
5. Click: "Yes, I trust the authors".
6. Select: Terminal -> New Terminal.
**Setup project virtual environment for Python libraries being installed only for our project:**
Create folder for the environment:
``` powershell
py -m venv venv
```
Activate newly created environment:
``` powershell
venv\Scripts\activate.bat
```
Activating the venv in the terminal makes it active for command-line operations, but for Jupyter in VS Code, you need to explicitly select it as the kernel. This ensures the notebook uses the packages installed in that venv, not your global Python.
7. Create folder for data: "data" and a folder for the code:"src" (next to "venv" folder). 
8. Create new file in "src" folder: "main.py".
9. Install recommended "Python" extension and in the "Extension Marketplace".
10. Create new file in "src" folder as alternative step by step execution file "main.ipynb". 
11. Run "main.py".
**If the environment is not changed because of permission problems:**
``` powershell
# Error message
File C:\Python repositories\DSP project\venv\Sc
ripts\Activate.ps1 cannot be loaded because running
 scripts is disabled on this system. For more infor
ecurityError: (:) [
   ], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess  
```
**Execute workaround for the problem:**
``` powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Activate newly created environment:
``` powershell
.\venv\Scripts\Activate.ps1
```
In PowerShell terminal there should be a confirmation of using local environment with (venv) prefix and also the pip list should be very short.
**Example:**
``` powershell
(venv) PS C:\Python repositories\Education project> 
```
12. Run "main.ipynb".
13. Select local not global virtual environment:
    "Python environments" -> venv(Python 3.13.7) venv\Scripts\python.exe (Recommended)
**What is the path to the Python executable you are using?:**
``` python
# What is the path to the Python executable you are using?
import sys
print(sys.executable)
```
**List and upgrade pip:**
``` powershell
# Upgrade pip (the package to install new packages)
python.exe -m pip install --upgrade pip
# Install new packages like pandas and numpy
pip install pandas
pip install numpy
# Install excel package
pip install openpyxl
# Install Jupyter Lab for Jupyter notebooks
pip install jupyterlab
# Check installed packages
pip list
```
**Run Jupyter Lab in the browser:**
``` powershell
jupyter lab
```
Run code in the [[jupy]]: **Shift + Enter**
**Use requirements file for installation:**
``` powershell
# Save the libraries as a list of requirements for the project
pip freeze > requirements.txt
# Install from frezed requirements
pip install -r requirements.txt
```
