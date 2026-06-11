#2.binary file handling



with open('/home/ndey/Python/microsoft-copilot-PAG-wzE6R7s-unsplash.jpg','rb') as f :
    data = f.read()
    print(type(data))
    #print(data) 

with open('/home/ndey/Python/File_Handling/sample5.jpg','wb') as f :
    f.write(data)

with open('/home/ndey/Python/microsoft-copilot-PAG-wzE6R7s-unsplash.jpg','rb') as f :
    chunk = 100
    df = f.read(chunk)
    with open('/home/ndey/Python/File_Handling/sample6.jpg','wb') as f2 :
        while len(df)> 0 :
            f2.write(df)
            df = f.read(chunk)