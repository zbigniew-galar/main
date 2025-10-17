**Create folder for the environment:**
``` powershell
py -m venv venv
```

**Activate newly created environment:**
``` powershell
venv\Scripts\activate.bat
```

**Activate newly created environment when we have an error:**
``` powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```
**Activate newly created environment:**
```
.\venv\Scripts\Activate.ps1
```

**List and upgrade pip:**
``` powershell
# Check installed packages
pip list
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
**Use requirements file for installation:**
``` powershell
# Save the libraries as a list of requirements for the project
pip freeze > requirements.txt
# Install from frezed requirements if needed
# pip install -r requirements.txt
```

**Run Jupyter Lab in the browser:**
``` powershell
jupyter lab
```
