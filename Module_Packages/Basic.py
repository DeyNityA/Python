import sys

# difference between built-in module and builitins module is that built-in module is a module that is written in C and is compiled into the Python interpreter, 
# while builtins module is a module that contains all the built-in functions of Python.
# built-in modules are not written in Python and are not available in the global namespace, we need to import them to use them.
# builtins module is always available in the global namespace, we can use the built-in functions without importing the builtins module.
print(sys.builtin_module_names)
print()
print(dir(__builtins__))

print()
# now we will not talk about the built-in modules and builtins module, because python don't search them in search path
# we will talk about the search path of Python. When we import a module, 
# Python will search for the module in the following order :-

#PYTHON SEARCH PATH
print('Python Will search importing Module in these PATH :-')
for e in sys.path :
    print(e)
print()
import Package1.Module1
from Package1 import Module1 
print(Package1.Module1.add(10,20))
#one package can contain multiple modules and we can import the modules in the package using the syntax import package_name.module_name. 
#We can also import specific functions or classes from the module using the syntax from package_name.module_name import function_name or class_name.
#one package can call another package and we can import the modules from the other package using the syntax import package_name.module_name.

calc = Package1.Module1.Calculator()
print(type(calc))
print(globals())


