# Module 1
def add(a,b) :
   return a+b

def subtract(a,b) :
   return a-b

def multiply(a,b) :
   return a*b

def divide(a,b) :
   if b == 0 :
      raise Exception("You can't divide by zero")
   return a/b

class Calculator :
   def __init__(self) :
      pass
   
   def add(self,a,b) :
      return a+b

   def subtract(self,a,b) :
      return a-b

   def multiply(self,a,b) :
      return a*b

   def divide(self,a,b) :
      if b == 0 :
         raise Exception("You can't divide by zero")
      return a/b
   
print(__name__)
calc1 = Calculator()
print(type(calc1))

if __name__ == "__main__" :
   print(add(10,20))
   print(subtract(10,20))
   print(multiply(10,20))
   try :
      print(divide(10,0))
   except Exception as e :
      print(e.args[0]) 

   calc = Calculator()
   print(calc.add(10,20))
   print(calc.subtract(10,20))
   print(calc.multiply(10,20))
   try :
      print(calc.divide(10,0))
   except Exception as e :
      print(e.args[0])
   
   print()