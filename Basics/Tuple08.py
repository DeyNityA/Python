t = (67,87,56,"ju")

print(type(t))
#tuples are immutable
#t[0]=90 is not possible

t2 = (67,87,56,"ju")

print(t2)

print(f"id of tuple t {id(t)}")
print(f"id of tuple t2 {id(t2)}")                  

for e in t :
    print(e)

#tuple slicing
print(t2[0:2])

a=90
b= "ko"
t5 = (a,b)
c,d = t5
print(t5)
print(c,d)

