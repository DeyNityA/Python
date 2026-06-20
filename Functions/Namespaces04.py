# Builtins namespace
# Global namespace
# Local namespace
# Enclosing namespace

if __name__ == "__main__" :

    print(dir(__builtins__)) # It will show the builtins namespace, which includes all the built-in functions and variables.
    x = 10

    def outer():
        print(x) # It will show the global variable x, as it is not defined in the local namespace of outer() function, it will look for it in the global namespace.
        y = 20
        e = 90
        def inner():
            nonlocal y # It will allow us to modify the variable y in the outer() function from the inner() function.
            y = y+78
            z = 30
            print(e) # It will show the variable e from the outer() function, as it is not defined in the local namespace of inner() function, it will look for it in the enclosing namespace of outer() function.
            print(dir()) # Local namespace of inner() will be shown in inner() and local namespace of outer() will be shown in outer(), but both will have access to the global namespace.
            print(locals())

        inner()
        print(dir()) # Local namespace of outer() will not be shown in inner() and vice versa, but both will have access to the global namespace.
        print(locals())

    class Hero :
        pass

    outer()
    print(dir()) # Global namespace, it will not show the local variables of the functions, it will only show the global variables and the built-in functions.
    print(globals())
    import datetime
    import sys
    print(dir()) # It will show the global namespace, which includes the imported module datetime.
    print(globals())

        # order of namespaces: Local -> Enclosing -> Global -> Built-in