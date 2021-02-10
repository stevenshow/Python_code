def track(f):
    def wrapper(*args1, **args2):
        wrapper.count += 1        
        return f(*args1, **args2)    
    wrapper.count = 0    
    return wrapper

def trace(func):
    def wrapper(*args1, **args2):
        print(func.__name__,'with',args1,args2)        
        return func(*args1, **args2)    
    return wrapper

def storeargs(arglist):
    def real(f):
        def wrapper(*args,**kwargs):
            key = str(args)+str(kwargs)
            if key in arglist:
                print(key + 'found in cache')
            else:   
                arglist.add(key)
            return f(*args,**kwargs)
        return wrapper
    return real

theargs = set()

@storeargs(theargs)
def fib(n):
    return n if n in (0,1) else fib(n-1) + fib(n-2)

print(fib(10))
print(theargs)

