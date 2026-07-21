
import sys

i=0

print(sys.getrecursionlimit())

def show_values():
    global i
    i = i+1
    print(i)
    show_values()

show_values() # RecursionError: maximum recursion depth exceeded in comparison 
# by default, the maximum recursion depth is 1000, we can change it using sys.setrecursionlimit() but it's not recommended
# as it can lead to a crash of the program.

