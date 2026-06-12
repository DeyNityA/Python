'''
import builtins
s = "jiii"
builtins.print(s)
builtins.print(builtins.len(s))
'''
# builtins module contains all the built-in functions of python. We can use these functions by importing builtins module and using the syntax builtins.function_name().
# but we don't need to import builtins module to use the built-in functions, we can directly use them without importing the module. 
# The built-in functions are always available in the global namespace.

import Module1

print(Module1.add(10,20))
print(Module1.subtract(10,20))
print(Module1.multiply(10,20))
try :
   print(Module1.divide(10,0))
except Exception as e :
   print(e.args[0]) 

calc = Module1.Calculator()
print(calc.add(10,20))
print(calc.subtract(10,20))
print(calc.multiply(10,20))
try :
   print(calc.divide(10,0))
except Exception as e :
   print(e.args[0])