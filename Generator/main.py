# generator 
# generator is a function that returns an iterator object, which can be used to iterate over a sequence of values.

#example of generator function
from collections.abc import Iterable, Iterator


def my_gen() :
    print('................................')
    yield 1
    yield 2
    yield 3

# using the generator
gen = my_gen() # function doesn't call this time.
print(type(gen)) # <class 'generator'>
print(isinstance(gen, Iterable)) # True
print(isinstance(gen, Iterator)) # True

for i in gen :
    print(i)

# best example related to file handling, we can use generator to read a file line by line, instead of reading the whole file at once,
# which can be memory intensive for large files.

#1. creating file of to-do list 
import json

ls = ['waking up at 6.00 am' , 'hit gym for at least 10 minutes' , '    ' , 'consume 80gm protein' , '    ' , 'sleep before 11 pm']

with open('todo.txt','w') as f :
    json.dump(ls,f)

#2. Let's assume that this todo file we are reading from server,
#   now assume you can't store this file in memory . but you need this information later on that session.



def read_file_generator(file) :
    with open(file,'r') as f :
        ls = json.load(f)
        for e in ls :
            if e.strip() :
                yield e


rfg = read_file_generator('todo.txt') 
print(type(rfg))
print()



for e in rfg :
    print(e)