from itertools import cycle
import re

def gameWinner(colors):
    # Write your code here
    lst = ['wendy', 'bob']
    pool = cycle(lst)   
    turn = next(pool)
    while len(colors) > 2:
        if turn == 'wendy':
            x = re.search("w{3}", colors)
            if x is not None:
                colors = colors[0 : x.start() : ] + colors[x.start() + 1 : :]
                print('wendy',colors)  
            else: return next(pool)
        else:
            x = re.search('b{3}', colors)
            if x is not None:
                colors = colors[0 : x.start() : ] + colors[x.start() + 1 : :]
            else: return next(pool)
        print(turn)

gameWinner('wwwbbbw')