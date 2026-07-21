str = "gyyhuhuhg  6 jkiop hjio hjoi yg"
str2 = "gyyhuhuhg jkiop hjio hjoi yg"

print(f"id of str {id(str)}")
print(f"id of str2  {id(str2)}")
print(str+"ko")

#strings are immutable
#str[1]="k" not possible
print(len(str))
print ("hu" in str)
print(str.index("hu"))

for e in str :
    print(e,e.isalnum())

print(ord("y")) #ascii code
print(chr(121))

# string slicing
print(str[2:6])

# string methods
s4 = str.capitalize()
print(s4)

s5 = str.title()
print(s5)

s6 = str.upper()
print(s6)

print(str.isalpha())

#-----split and join--------#
ls = str.split(" ")
print(type(ls))
print(ls)

str8 = " ".join(ls)
print(type(str8))
print(str8)