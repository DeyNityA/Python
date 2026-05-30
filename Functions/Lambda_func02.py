square = lambda a : a**2

print(square)

print(square(6))

# lamda function uses in sorted func

l = ["Dhoni Singh Mahendra" , "Kohli Virat", "Sharma Rohit", "Tendulkar Sachin" , "Raina Suresh"]

print(sorted(l))
print(sorted(l, key = len, reverse = True))
print(sorted(l,key = lambda e : e.split(" ")[::-1][0][0])) #sorting based surname first letter

'''
Higer order functions - a function that takes another function as an argument or returns a function as a result is called a higher-order function.
'''
#function returning function

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

func = outer_function(5)
print(func(3))

func2 = lambda x : lambda y : x+y
print(func2(6)(8))

#passing function as an argument to another function
def add_func(func,a,b) :
    return func(a,b)

def add_in_func(x,y) :
    return x+y


print(add_func(add_in_func,4,5))
print(add_func(lambda x,y : x+y, 4,5)) #using lambda function as an argument to another function


# IFFE - Immediately Invoked Function Expression - a function that is defined and called immediately after its definition. 
# IFFE is a common pattern in JavaScript, but it can also be used in Python with lambda functions. but in Python, 
# we can't use the def keyword to define a function and then call it immediately, but we can achieve a similar effect using lambda functions.

result = (lambda x, y : x + y)(10, 20)
print(result)   

# if else in lambda function

is_even = lambda x : True if x%2==0 else False
print(is_even(4))

# filtering a list using lambda function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x : x%2==0, numbers)

print(type(even_numbers))
for e in even_numbers :
    print(e)
print(tuple(even_numbers)) # filter returns an iterator, we can convert it to a list or tuple
# we can consume the iterator only once, after that it will be empty, that's why we get an empty tuple.

# mapping a list using lambda function
squared_numbers = map(lambda x : x**2, numbers)
print(list(squared_numbers)) # map returns an iterator, we can convert it to a list

# reducing a list using lambda function

from functools import reduce
product = reduce(lambda x,y : x*y, numbers)
print(product)

max_num = reduce(lambda x,y : x if x>y else y, numbers)
print(max_num)

min_num = reduce(lambda x,y : x if x<y else y, numbers)
print(min_num)