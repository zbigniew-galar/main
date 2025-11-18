### Installing Python and VS Code on **Windows** (Windows 10 or Windows 11)
#### Step 1: Install Python (the programming language)
1. Open your web browser (Edge, Chrome, Firefox…) and go to:  
   https://www.python.org/downloads/
2. The website will automatically show you the big yellow button that says **“Download Python 3.12.x”** or **3.13.x** (the newest version).  
   Click that big yellow button.
3. When the download finishes, double-click the file that starts with `python-3.xx.x-amd64-installer.exe`
4. **VERY IMPORTANT WINDOW APPEARS** →  
   - Put a checkmark in the box that says **“Add python.exe to PATH”** (it’s at the bottom)  
   - Then click **“Install Now”** (don’t click Customize)
5. A setup window will appear and install Python. Wait until it says “Setup was successful”.
6. Click “Close”.
7. Test if it worked:  
   - Press the Windows key, type `cmd`, and open **Command Prompt**  
   - Type this and press Enter:  
```
python --version
```
   - You should see something like `Python 3.12.7` or higher → Python is installed!
#### Step 2: Install Visual Studio Code
1. Open your browser again and go to:  
   https://code.visualstudio.com/
2. Click the big blue button **“Download for Windows”**
3. When the download finishes, double-click the file `VSCodeUserSetup-x64-x.xx.x.exe`
4. A setup wizard starts → click “I accept the agreement” → Next → Next → Next
5. **Important**: On the page “Select Additional Tasks” put checkmarks in:
   - Add “Open with Code” action to Windows Explorer file context menu
   - Add “Open with Code” action to Windows Explorer directory context menu  
   - **Add to PATH** (this one is super important!)
1. Then keep clicking Next → Install → Finish
2. VS Code will open automatically (or you can find it in the Start menu).
#### Step 3: Install the Python extension inside VS Code
1. Open VS Code
2. On the left sidebar click the Extensions icon (looks like four squares)
3. In the search box type: `Python`
4. The first result will be “Python” by Microsoft (millions of downloads) → click **Install**
5. Wait until it finishes installing (it will also install Pylance automatically)
Done! You can now create Python files and run code in VS Code on Windows.

## Troubleshooting – What to do if something goes wrong

| Problem | How to fix it |
| ------- | ------------- |
| When I type `python` in Command Prompt it says “python is not recognized” | You forgot to tick “Add python.exe to PATH”. Fix: <br>1. Find the python installer file again and run it<br>2. Choose “Modify”<br>3. Tick “Add Python to PATH” → Next → Install |
| VS Code says “Python interpreter not selected” or can’t find Python | 1. Press Ctrl + Shift + P<br>2. Type “Python: Select Interpreter”<br>3. Choose the one that says `Python 3.x.x` (usually at the top) |
| I get a warning “Running as Administrator” or antivirus blocks it | Right-click the installer → “Run as administrator”<br>Or temporarily turn off antivirus (only for the install) |
| Nothing happens when I double-click the installer | Download the file again – sometimes it gets corrupted |
| I have two Pythons and it’s confused (old one + new one) | Uninstall the old Python from Settings → Apps → search “Python” → uninstall everything except the newest one |
| VS Code opens but looks weird / extensions won’t install | Close VS Code completely → right-click its icon → “Run as administrator” once, then install the extension |
| I can’t type in the VS Code terminal (black screen) | Click the dropdown at the top of the terminal and choose “Command Prompt” or “PowerShell” instead of Git Bash |


### Installing Python and VS Code on **macOS** (MacBook or iMac)
#### Step 1: Install Python (the newest version)
1. Open Safari or Chrome and go to:  
   https://www.python.org/downloads/
2. You will see a big yellow button **“Download Python 3.12.x”** or **3.13.x** → click it
3. A file called `python-3.xx.x-macos.pkg` will download.
4. Double-click that file (it’s usually in your Downloads folder)
5. The installer opens → click Continue → Continue → Agree → Install  
   (it will ask for your Mac password – the one you use to log in or install apps)
6. Wait until it says “The installation was successful” → Close
7. Test it:
   - Open **Terminal** (press Cmd + Space, type “Terminal”, press Enter)
   - Type and press Enter
```
python3 --version
```
   - You should see `Python 3.12.x` or higher → perfect!
#### Step 2: Install Visual Studio Code
1. Go to:  
   https://code.visualstudio.com/
2. Click the big blue button **“Download for Mac”** (it will say “Apple Silicon” or “Intel” – it chooses the right one automatically)
3. When the download finishes, open the file `VSCode-darwin-universal.zip` (or similar) from your Downloads folder
4. A new window opens with “Visual Studio Code.app” → drag that app into your **Applications** folder
5. You can now close the app from Launchpad or from Applications folder.
#### Step 3: Install the Python extension in VS Code
1. Open Visual Studio Code
2. Click the Extensions icon on the left (four squares)
3. Search for `Python`
4. Install the official “Python” extension by Microsoft (the one with millions of downloads)
5. Wait for it to finish (it will also install Pylance)
#### Optional but recommended: Make VS Code easier to open from Terminal
1. In VS Code press `Cmd + Shift + P` → type “shell command”  
2. Choose **“Shell Command: Install 'code' in PATH”** → press Enter  


   Now you can open any folder in VS Code just by typing `code .` in Terminal!

You’re all set! Your Mac now has Python and VS Code ready for learning programming.

## Troubleshooting – Mac problems & fixes

| Problem | How to fix it |
| ------- | ------------- |
| Terminal says `python3: command not found` | The installer didn’t finish properly. Run the `.pkg` file again and make sure you typed your password correctly. |
| Mac says “Visual Studio Code.app can’t be opened because Apple cannot check it for malicious software” | Right-click the app → choose “Open” → click “Open” again on the warning (you only have to do this once) |
| VS Code won’t start at all (bounces once in Dock then disappears) | Go to Applications → right-click VS Code → Show Package Contents → Contents → MacOS → double-click “Electron” (this forces it to open) |
| Extensions won’t install / spinning forever | Close VS Code → reopen it while holding Cmd + Shift (this disables all extensions temporarily) → then install Python extension again |
| When I run code it says “Permission denied” or “zsh: command not found python3” | Close Terminal completely → reopen it (macOS needs a fresh terminal after installing Python) |
| I have the old macOS Python 2.7 and it’s confusing VS Code | Always use `python3` (not just `python`). In VS Code press Cmd + Shift + P → “Python: Select Interpreter” → choose the one that says `/usr/local/bin/python3` or `/opt/homebrew/bin/python3` |
| VS Code says “The Python extension failed to load” | Restart your Mac (seriously – this fixes 90% of Mac extension problems) |
| I can’t drag VS Code to the Dock | Open it first from Applications, then right-click the icon in the Dock → Options → Keep in Dock |
