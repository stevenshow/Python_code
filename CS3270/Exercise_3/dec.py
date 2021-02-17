'''Decorates the fib function so that it reduces the amount of calls
made, and also logs the answers to each fib number
Created by: Steven Schoebinger 02/16/2021'''
# pylint: disable=invalid-name
import os
import functools
path = os.path.dirname(__file__)

def track(f):
    '''Tracks the number of function calls made to the fib function
    and caches the results so it can return the result if the call
    has already been made'''
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        key = str(args)+str(kwargs)
        if key in wrapper.arglist:
            print(key + 'found in cache')
        else:
            wrapper.count += 1
            wrapper.arglist[key] = f(*args,**kwargs)
        return wrapper.arglist[key]
    wrapper.count = 0
    wrapper.arglist = {}
    return wrapper

def log(f):
    '''Creates a log file and places the answers to each fib number in
    sequence'''
    @functools.wraps(f)
    def wrapper(*args,**kwargs):
        with open(path + '/log.txt', 'a+') as logfile:
            key = str(args)+str(kwargs)
            answer = f(*args, **kwargs)
            logfile.write(f.__name__ + key + ' = ' + str(answer) + '\n')
        return answer
    return wrapper

@track
@log
def fib(n):
    '''Returns the fib number'''
    return n if n in (0,1) else fib(n-1) + fib(n-2)
print(f'{fib(10)}, calls = {fib.count}')
