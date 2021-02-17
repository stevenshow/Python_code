import os
path = os.path.dirname(__file__)

def track(f):
    def wrapper(*args1, **args2):
        #print(wrapper.count)      
        wrapper.count += 1
        return f(*args1, **args2)    
    wrapper.count = 0    
    return wrapper

def log(arglist):
    def real(f):
        def wrapper(*args,**kwargs):
            with open(path + '/log.txt', 'a+') as logfile:
                key = str(args)+str(kwargs)
                if key in arglist:
                    print(key + 'found in cache')
                    return arglist[key]
                else:
                    arglist[key] = f(args[0])
                    #logfile.write(f.__name__ + key + ' = ' + str(arglist[key]) + '\n')
                    return arglist[key]
            return f(*args,**kwargs)
        return wrapper
    return real

arglist = {}
@track
@log(arglist)
def fib(n):
    return n if n in (0,1) else fib(n-1) + fib(n-2)

print(f'{fib(10)}, calls = {fib.count}')