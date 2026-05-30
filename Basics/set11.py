s = {89,56,34,"ji",99.89,7,55,34}
#unordered set - dont't have any index, only stores unique value

print(s)

#empty set
s1 = set()
print(s1)

s1.add(60)

print(60 in s1)

for e in s :
    print(e)

l = [78,90,67,34]
l2 = [78,45,90,67]
s3 = set(l)
s4 = set(l2)

print(s3.intersection(s4))
print(s3.union(s4))

s4.remove(45)
print(s4)
