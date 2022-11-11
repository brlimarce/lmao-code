<!-- Heading -->
# **lmao-code**
🤖 Interpreter for LOLCODE using **Python.**
<br /> <br />

<!-- Installation -->
## **Dependencies**
- - -
<br />

### **A. Virtual Environment**
- - -
**Activate** the virtual environment (venv) before **running the Python file.** Otherwise, the installed dependencies won't work.

```bash
# * Linux
# Activate the virtual environment (VENV).
source lenv/bin/activate

# * Windows
# Install virtual environment (must have Python).
pip install virtualenv

# Activate the virtual environment (VENV).
# ? Can also be: wenv/scripts/activate
wenv/Scripts/activate

# Deactivate VENV (both Windows and Linux).
deactivate
```
<br />

### **B. Install Dependencies**
- - -
To install libraries, modules, etc., run VENV first **(see Section A).** Then, install and **update requirements.txt**

```bash
# Install the library, module, etc.
pip install <library_name>

# Update the list of dependencies.
pip freeze > requirements.txt

# Run this IF you want to update dependencies in your venv.
pip install -r requirements.txt
```