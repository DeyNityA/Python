
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