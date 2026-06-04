import math

def simplify(func) :
    def inner(*args,**kargs) :
        res = func(*args,**kargs)
        ls = res.split("/")
        num = int(ls[0])
        den = int(ls[1])
        cf = math.gcd(num,den)
        return f"{int(num/cf)}/{int(den/cf)}"
    return inner




class Fraction :
    def __init__(self,a,b):
        self.numerator = a
        self.denominator = b
    
    
    def __add__(self,other) :
        f = Fraction(int(self.numerator*other.denominator+other.numerator*self.denominator),int((self.denominator*other.denominator)))
        return f
    
    @simplify
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    


f1 = Fraction(3,4)
f2 = Fraction(5,6)

f3 = f1+f2

print(f3)

# private members of a class, we can access them using name mangling, but it is not recommended, because it is not a good practice.

class A :
    def __init__(self) :
        self.__a = 5        
a = A()
# print(a.__a) # AttributeError: 'A' object has no attribute '__a'
print(a._A__a)

# private methods of a class, we can access them using name mangling, but it is not recommended, because it is not a good practice.
class B :
    def __init__(self) :
        self.__a = 5
    
    def __private_method(self) :
        print("This is a private method")

b = B()
# b.__private_method() # AttributeError: 'B' object has no attribute '__private_method'
b._B__private_method()