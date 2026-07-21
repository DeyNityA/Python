'''we can install them system-wide:

sudo apt install python3-numpy
sudo apt install python3-pandas

Packages are usually stored under: /usr/lib/python3/dist-packages/numpy/__init__.py 
or /usr/local/lib/python3.12/dist-packages/numpy/__init__.py

This makes the packages available to all users and all Python projects on the machine.

Problem:
Suppose:

Project A needs NumPy 1.26
Project B needs NumPy 2.0

A system-wide installation can only have one version managed by Ubuntu packages.

So different projects may conflict with each other.
'''

'''
2. Why use a Virtual Environment (venv)?

A virtual environment creates an isolated Python environment for a project.

Think of it like:

System Python
│
├── Project A
│   ├── NumPy 1.26
│   └── Pandas 2.1
│
└── Project B
    ├── NumPy 2.0
    └── Pandas 2.3
'''

'''
sudo apt install python3-venv
mkdir myproject
cd myproject
python3 -m venv .venv
source .venv/bin/activate

pip is a package manager for Python.

It is a tool that downloads and installs Python packages (modules/libraries) from the Python Package Index (PyPI). basically used in virual env.
'''


import numpy as np
import sys
import pip

print(dir())

print()
print(globals())

print()
print(sys.path)