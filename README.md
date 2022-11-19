<!-- Heading -->

# **lmao-code**

🤖 Interpreter for LOLCODE using **Python.**
<br /> <br />

<!-- Installation -->

## **Dependencies**

### **A. Virtual Environment**

---

**Activate** the virtual environment (venv) before **running the Python file.** Otherwise, the installed dependencies won't work.

```bash
# 1. Install the package `virtualenv`.
pip install virtualenv

# 2. Create your own VENV (do this only ONCE).
virtualenv venv

# 3. Activate your VENV.
source venv/bin/activate # Linux
venv/Scripts/activate # Windows

# 4. Deactivate your VENV (to turn it off).
deactivate
```

### **B. Install Dependencies**

---

To install packages, **run VENV first** (see Section A). Then, **update requirements.txt** after installing that package.

```bash
# Install the library, module, etc.
pip install <library_name>

# Update the list of dependencies.
# ! Done because the package will only reflect on OUR VENV (and not the others').
pip freeze > ../requirements.txt

# Run this IF you want to update dependencies in your venv.
# ! Done when one of us decides to add a package.
pip install -r ../requirements.txt
```
