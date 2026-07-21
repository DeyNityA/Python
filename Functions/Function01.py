def sum(a,b) :
    return a+b

#function is also a object, we can assign it to a variable, we can pass it as an argument to another function, we can return it from another function.
print(isinstance(sum,object))

print(type(sum))
fsum = sum

print(fsum)
print(id(fsum))
print(id(sum))

res = fsum(5,9)
print(res)

#local & global variables
c = 78
print(globals())

def local_scope() :
    a = 6
    print(locals())
    b = 8
    global c 
    c = c+1 
    # If not mentioned global,
    #UnboundLocalError: cannot access local variable 'c' where it is not associated with a value
    print(a,b,c)

a = 9

print(local_scope())
print(a,c)

#default arguments(c,d ), it should be always at the end of the parameter list
#positional arguments(a,b)
def sum(a,b,c=0,d=0) :
    return a+b+c+d

print(id(sum))

print(sum(5,6))
print(sum(5,6,7))
print(sum(5,6,7,8))

#variable length positional/keyword arguments
def sum(*args) :
    print(f"{args} -> {type(args)}")
    res = 0
    for e in args :
        res+=e
    return res

print(sum(3,8,7,5,7,4,4))

def sum(**kargs) :
    print(f"{kargs} -> {type(kargs)}")
    res = 0
    for k,v in kargs.items() :
        res+=v
    return res

print(sum(Math = 99, Bengali = 67, English = 80))

# order = positional args -> variable length positional args -> keyword args -> variable length keyword args -> default args

#default args alwayas set for first time, if we change the value of default arg, it will change for all the calls to the function, 
#because default args are stored in the function object, not in the local scope of the function.

def func(a,ls = []) :
    print(locals())
    ls.append(a)
    print(ls)

func(5)
func(6)
