i = 1

while i<10 :
    if i==9 :
        print(i)
    else :
        print(i,end=" ")
    i+=1



for j in range(1,11,1) :
    print(j)

print()

'''
control statements
1.continue
2.break
'''

for k in range(10,1,-2) :
    print(k,end=" ")
    if k ==4 :
        print()
        continue
    print(k+1)

print()

for k in range(10,1,-2) :
    print(k,end=" ")
    if k ==4 :
        print()
        break
    print(k+1)