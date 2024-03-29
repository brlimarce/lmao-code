<!-- Heading -->
<img src="assets/banner.png"> <br />

<p align="center"> 🐱&ensp;An esoteric programming interpreter </p>
<hr />

<!-- Installation -->
### **🍃&ensp;Virtual Environment**
This repository relies on using a **virtual environment (venv)** so that the downloaded packages don't reflect on the machine. <br />

**Activate** the virtual environment (venv) before **running the Python file.** Otherwise, the installed dependencies won't work.

```bash
# 1. Install the package `virtualenv`.
pip install virtualenv

# 2. Create your own VENV (do this only ONCE).
virtualenv venv

# 3. Activate your VENV.
source venv/bin/activate # Linux
venv/Scripts/activate # Windows

# 4. Turn off your VENV.
deactivate
```
### **📤&ensp;Dependencies**
To install packages, **run VENV first** *(see Section A).* Then, **update requirements.txt** after installing that package.

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
### **🐱&ensp;Run the Program**
To run the program, you must have your **VENV activated** and **packages installed.** *(see above)* Then, enter the following command:
```
python main.py
```