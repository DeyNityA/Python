import sys


print(sys.getrefcount(997809.457986))

a = 997809.457986
print(id(a))
def show() :
    b = 997809.457986
    print(id(b))
    print(__name__)
    print(sys.getrefcount(997809.457986))


print(sys.getrefcount(997809.457986))
show()
print(show.__name__)
print(globals())