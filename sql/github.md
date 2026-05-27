### Git workflow with Feature branches
**In MS Visual Studio Code create a Git bash terminal:**
``` bash
git init
```
**Copy git URL found under the green Code button:**
``` bash
 git remote add origin https://github.com/zbigniew-galar/forecasting.git
```
**Change the name of the main branch from "master" to "main":**
``` bash
git branch -m master main
```
**Add exclusions list file from version tracking starting with environment folder:**
``` bash
echo "venv/" > .gitignore
```
**Staging the Git Ignore file to track all files in src folder:**
``` bash
git add src/ .gitignore
```
**Make initial commit to repository:**
``` bash
git commit -m "Initial commit: Add project structure and .gitignore"
```
**Check the status:**
``` bash
git status
```
**Pull any files from GitHub main repository to local:**
``` bash
git pull origin main
```
**Push your local changes to remote repository:**
``` bash
git push -u origin main
```
**Force push into remote branch only use when necessary:**
```bash
git push -f origin main
```
**Start a new branch:**
``` bash
git checkout -b documentation
```
**Including change in a file to a new branch:**
``` bash
git add src/models.py
```
**Commit with description changes:**
``` bash
git commit -m "Comments added in the main file."
```
**Push all commited changes to GitHub:**
``` bash
git push origin documentation
```
**Change back to main branch:**
``` bash
git checkout main
```
**Update local based on the code on GitHub in the main branch:**
``` bash
git pull origin main
```
**Example update directly to main:**
``` shell
git add src/models.py
git commit -m "Refresh"
git push origin main
```
