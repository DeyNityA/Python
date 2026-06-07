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
        
    def openTrunk() :
        print("Trunk is open now")

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