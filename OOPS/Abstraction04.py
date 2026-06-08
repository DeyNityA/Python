from abc import ABC, abstractmethod

class Duck(ABC) :
    @abstractmethod
    def quack(self) :
        pass    

    def swim(self) :
        print("Swimming...")

class Person(Duck) :
    def quack(self) :
        print("I am a person, I can quack like a duck!")

p = Person()
p.quack()
p.swim()

#abstract classes cannot be instantiated, but they can be subclassed, and the subclass can be instantiated.
#interface is a class that has only abstract methods, and it cannot have any concrete methods,
#but in Python, we can have both abstract and concrete methods in the same class, so we can say that Python does not have a separate concept of interface, 
#but we can achieve the same functionality by using abstract classes.