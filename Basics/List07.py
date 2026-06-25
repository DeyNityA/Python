import copy

l = [67,90,23,"a","yui",-9,True]*2
print(type(l))
print(len(l))

for i in range(0,len(l)) :
    print(l[i],end=" ")

print()

for i in range(1,len(l)) :
    print(l[-i],end=" ")

print()

l.append(9)
l.append(["op",90])
print(l)
l.extend([89,87])
print(l)

l.pop()
print(l)
l.pop(3) #will remove by index
print(l)

l.remove(23) #will remove by element,if not there will give error
print(l)

l.insert(4,345678)
print(l)

l.reverse()
print(l)

#l.sort() will work only for same datatypes.

print(l.index(67))
print (67 in l)

l.reverse()
print(l)

# lists are mutable


#----------- shallow copy ---------------#

a = 1467800000006789.8
b = 1467800000006789.8
print(f"id of a is {id(a)}")
print(f"id of b is {id(b)}")
print(a is b)
# in Python, values like small integers and short strings(immutable objects) are often reused by the interpreter to save memory and speed up the program.
# this is interning of memory addresses for immutable data types.

l1 = [[5,6,7],[6,7,8],[9,10,11]]

print()
print(f"id of l1 is {id(l1)}")


for ml in l1 :
    print(f"id of {ml} is {id(ml)}")
    for e in ml :
        print(f"id of {e} is {id(e)}")

#l2 = l1.copy() #shallow copy
l2 = copy.copy(l1)

print()
print(f"id of l2 is {id(l2)}")
for ml in l2 :
    print(f"id of {ml} is {id(ml)}")
    for e in ml :
        print(f"id of {e} is {id(e)}")  

#--------------deep copy-------------#
l3=copy.deepcopy(l1)
print()
print(f"id of l3 is {id(l3)}")
for ml in l3 :
    print(f"id of {ml} is {id(ml)}")
    for e in ml :
        print(f"id of {e} is {id(e)}")  

#-------List Comprehension---------#
my_list = [i for i in range(1,100)]
print(my_list)

my_list2 = [i if i%2==0 else 0 for i in range(1,100)]
print(my_list2)

my_list3 = [i for i in range(1,100) if i%2==0]
print(my_list3)

mylist4 = [i**2 if i%2 ==0 else i**3 if i%3==0 else i for i in range(1,100)]
print(mylist4)

#----------list slicing-----------#
my_list5 = my_list3[0:4:2]
print(my_list5)