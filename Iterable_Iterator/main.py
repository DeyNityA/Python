#Iterable - An iterable is an object that can be iterated over, meaning you can loop through its elements one at a time.
#Iterator - An iterator is an object that represents a stream of data. It returns the next

from collections.abc import Iterable, Iterator
import sys


ls = [3,7,8,4,5,9,7,5,6,7,4,8,4,7,5,6,7,8,9,4,5,6,7,8,9,4,5,6,7,8,9]
print(type(ls)) # <class 'list'>
print(isinstance(ls, list)) # True
print(isinstance(ls, object)) # True
print(isinstance(ls, Iterable)) # True
print(isinstance(ls, Iterator)) # False

print(sys.getsizeof(ls)) 

it = iter(ls)
print(type(it)) # <class 'list_iterator'>
print(isinstance(it, Iterable)) # True
print(isinstance(it, Iterator)) # True

print(sys.getsizeof(it))

# how for works in python, it creates an iterator object and calls the next() function on the iterator object until it raises a StopIteration exception.
while True:
    try:
        print(next(it))
    except StopIteration:
        break

# an iterable should always have an __iter__() method that returns an iterator object, 
# and an iterator should always have a __next__() method that returns the next element in the sequence.
# an iterator also have a __iter__() method that returns itself, so that it can be used in a for loop or any other context that requires an iterable.

print(dir(ls))
print()
print(dir(it))

x = range(1,10)
print(type(x)) # <class 'range'>
print(isinstance(x, Iterable)) # True
print(isinstance(x, Iterator)) # False
print(dir(x))

# all iterables are not iterators, but all iterators are iterables. An iterable is an object that can be iterated over.

# creating custom iterable and iterator object
class custom_list :
    def __init__(self,*args) :
        self.elements = args

    def __iter__(self):
        return custom_list_iterator(self)

    def __str__(self) :
        return f"{list(self.elements)}"

class custom_list_iterator :
    def __init__(self,itearable_obj : custom_list) :
        self.data = itearable_obj
        self.index = 0

    def __iter__(self) :
        return self
    
    def __next__(self) :
        if self.index < len(self.data.elements) :
            res = self.data.elements[self.index]
            self.index +=1
            return res
        
        raise StopIteration
    
ls1 = custom_list(2,9,7,6,0,7,4,9,5,9,5,7,5,4,3,7,8,4,4,5)
print(ls1)
print(type(ls1))
print(sys.getsizeof(ls1))
print(isinstance(ls1,Iterable))
l = iter(ls1)
print(sys.getsizeof(l))
for i in ls1 :
    print(i)