# python do absolutely nothing at runtime.

class vehicle :
    def __init__(self,maxSpeed) :
        self.__maxSpeed = maxSpeed

    def honk(self) :
        print("Beep! Beep!")

    def get_maxSpeed(self) :
        return self.__maxSpeed

class car(vehicle) :
    #constructor overriding
    def __init__(self,maxSpeed,numberOfDoors) :
        super().__init__(maxSpeed)
        self.numberOfDoors = numberOfDoors
    
    #method overriding
    def honk(self) :
        print("Car is honking! Beep! Beep!")
        
    def openTrunk(self) :
        print("Trunk is open now")

    def get_numberOfDoors(self) :
        return self.numberOfDoors

class Truck(vehicle) :   
    def caryLoad() :
        print("It can cary load")


'''
what gets inherited
1. constructor
2. Non private attributes
3. Non private methods
'''

c = car(100,4)
#print(c._vehicle__maxSpeed)
c.honk()
print(c.get_maxSpeed())
print(isinstance(c,car)) # True
print(isinstance(c,vehicle)) # True
print(c.__class__) # <class '__main__.car'>

v= vehicle(120)
print(isinstance(v,car)) # False
print(isinstance(v,vehicle)) # True
v.honk()
v.__class__ = car # it is not recommended
print(isinstance(v,car)) # True
print(isinstance(v,vehicle)) # True
v.honk() # Car is honking! Beep! Beep!
v.openTrunk() # Trunk is open now
# print(v.get_numberOfDoors()) # AttributeError: 'car' object has no attribute 'numberOfDoors'. Did you mean: 'get_numberOfDoors'?


t = Truck(80)
t.honk()
print(t.get_maxSpeed())

#multiple inheritance and method resolution order (MRO)
class A :
    def show(self) :
        print("In A")
class B :
    def show(self) :
        print("In B")
class C(A,B) :
    pass    
c = C()
c.show() # it will print "In A" because A is the first parent class in the definition of C, so it will look for the show method in A first and then in B

#method resolution order (MRO) is the order in which Python looks for a method in a hierarchy of classes. 
print(C.__mro__)


'''
polymorphism
1. method overloading - not supported in python
2. method overriding - supported in python
3. operator overloading - supported in python
'''


class E :
    def show(self) :
        print("In E")
class F(E) :
    def show(self,y) :
        print("In F",y)

f = F()
f.show(10) 

'''
overriding does not mean that method signatures should be same, it means that method name should be same, 
so in the above example, the show method in F overrides the show method in E, even though the method signatures are different.
'''

'''
overloading is not supported in python, but we can achieve it by using default arguments or variable length arguments.
oveloading method should be defined in the same class.
'''

# duck typing and strong typing
# duck typing is a concept in which the type of an object is determined by its behavior rather than its class. 
# strong typing is a concept in which the type of an object is determined by its class and it does not allow implicit type conversion.

class Duck :
    def quack(self) :
        print("Quack! Quack!")
class Person :
    def quack(self) :
        print("I am a person, I can quack like a duck!")

class Car :
    def honk(self) :
        print("Beep! Beep!")

def make_it_quack(duck) :
    duck.quack()

d = Duck()
p = Person()
c= Car()

make_it_quack(d) 
make_it_quack(p) 
# make_it_quack(c) # AttributeError: 'Car' object has no attribute 'quack'

#strong typing
# in strong typing, we can check the type of the object before calling the method, so that we can avoid the error at runtime.
# duck:DUCK is a type hint, it is not a strict type checking, it is just a hint for the programmer and the IDE, 
# it does not enforce the type checking at runtime. it will still allow us to call the method on any object,
def make_it_quack_strong(duck:Duck) :
    if not isinstance(duck,Duck) :
        raise TypeError("Expected a Duck object")
    duck.quack()

make_it_quack_strong(d)
# make_it_quack_strong(p) # TypeError: Expected a Duck object