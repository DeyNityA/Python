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
