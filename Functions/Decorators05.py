
import re
import time


def timer(func) :
    def wrapper (*args,**kargs) :
        start = time.time()
        res = func(*args,**kargs)
        end = time.time()
        duration = end - start
        if duration < 0.001:
            time_str = f"{duration * 1_000_000:.3f} µs"
        elif duration < 1:
            time_str = f"{duration * 1000:.3f} ms"
        else:
            time_str = f"{duration:.3f} s"
            
        print(f"{func.__name__} for {list(args)} ran in {time_str}")
        return res
    return wrapper

@timer  
def func(n) :
    time.sleep(n)

#func = timer(func)


@timer
def fact(n) :
    res = 1
    
    for i in range(n,0,-1) :
        res = res*i

    return res

print(func(7))

print(fact(5))

# decorators with arguments
def typecheck(obj) :
    def outer_wrapper(func) :
        def inner_wrapper(*args,**kargs) :
            for e in args :
                if type(e) != obj :
                    return f"You are giving wrong input type for {func.__name__} function"
            return func(*args,**kargs)
        return inner_wrapper
    return outer_wrapper


@typecheck(int)
def add(a,b,c) :
    return a+b+c;

print(add(5,8,9.9))

