#1.text file(utf-8 handling in python)
# if the file is not present, it will be created or if the file is present, it will be overwritten
f = open('sample.txt','w')
f.write('Hello world\nhow are you?')
f.close()


f = open('sample.txt','a')
f.write('\nI\'m fine, thank you!')
f.close()

l= ["Are Baap re\n","Ye kya ho gya"]

f= open("/home/ndey/Python/File_Handling/sample.txt","w")
f.writelines(l)
f.close()

f = open('sample.txt','r')
ps =f.read()
f.seek(0)  # move the file pointer to the beginning of the file
ps2 =f.read(5) # it will return the first 5 characters because the file pointer is now at the beginning of the file
print(ps)
print(ps2)
f.close()

f = open('sample.txt','r')
line = f.readline() # it will return the first line in the file

while line != "" :
    print(line,end="")
    line = f.readline() # it will return the next line in the file
f.close()
print()
f= open('/home/ndey/Python/File_Handling/sample.txt','r')

for line in f :
    print(line,end="")
f.close()
print()


# using context manager to handle files
# with statement is used to handle files in python. it will automatically close the file after the block of code is executed
with open('/home/ndey/Python/File_Handling/sample.txt','r') as f :
    for line in f :
        print(line,end="")

print()
# serialization and deserialization
# why we need serialization and deserialization?
# serialization is the process of converting a python object into ajson format.t 
# deserialization is the process of converting a json format into a python object.
# problem :
# passing list or dictionary to a file and then reading it back as a list or dictionary or int or float or any other data type is not possible because the file will store the data as a string. 

dict1 = {"name":"ndey","age":22,"city":"delhi"}

with open('/home/ndey/Python/File_Handling/sample2.txt','w') as f :
    f.write(str(dict1))

with open('/home/ndey/Python/File_Handling/sample2.txt','r') as f :
    data = f.read()
    print(type(data))
    dict2 = eval(data)  # convert the string back to a dictionary
    print(dict2.get("name"))

#converting string to a list or dictionary is not a good practice because it can lead to security issues.
import json
with open('/home/ndey/Python/File_Handling/sample3.txt','w') as f :
    json.dump(dict1,f) # it will convert the dictionary to a json format and write it to the file

with open('/home/ndey/Python/File_Handling/sample3.txt','r') as f :
    dict2 = json.load(f) # it will convert the json format back to a python object
    print(dict2.get("name"))

list1 = [1,2,3,4,5]
with open('/home/ndey/Python/File_Handling/sample4.txt','w') as f :
    json.dump(list1,f)

with open('/home/ndey/Python/File_Handling/sample4.txt','r') as f :
    list2 = json.load(f)
    print(type(list2))

# custom serialization and deserialization
class Person :
    def __init__(self,name,age) :
        self.name = name
        self.age = age
    
def serialize_person(person) :
    return {"name":person.name,"age":person.age}

def deserialize_person(data) :
    return Person(data["name"],data["age"])

person1 = Person("ndey",22)
with open('/home/ndey/Python/File_Handling/sample7.txt','w') as f :
    json.dump(person1,f,default=serialize_person)

with open('/home/ndey/Python/File_Handling/sample7.txt','r') as f :
    data = json.load(f,object_hook=deserialize_person)
    print(type(data))
    print(data.name)

