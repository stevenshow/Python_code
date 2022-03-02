'''
Project 6: Hashing & Caching (Instructor Solution)
Author: Georeg Rudolph
Date: 15 Apr 2021
This program needs to be run from command line
terminal
'''

from sys import argv
from time import perf_counter as timer
from hashmap import HashMap

PERSON_WT = 200
call_count = 0
cache_hits = 0

cache = HashMap()

def weight_on(r,c):
    global call_count
    global cache_hits

    call_count += 1
    try:
        weight = cache.get((r,c))
        #cache_hits += 1
        return weight
    except KeyError:
        pass


    if (r,c) == (0,0):
        #cache.set((r,c),0)
        return 0
    if c == 0:
        weight = PERSON_WT/2 + weight_on(r-1,0)/2
        #cache.set((r,c), weight)
        return weight
    if c == r:
        weight = PERSON_WT/2 + weight_on(r-1,c-1)/2
        #cache.set((r,c), weight)
        return weight
    weight = PERSON_WT + weight_on(r-1,c-1)/2 + weight_on(r-1,c)/2
    #cache.set((r,c), weight)
    return weight

def pprint(weights):
    print(" ".join([f'{i:<6.2f}' for i in weights]))

def main():
    start = timer()
    rows = int(argv[1])
    for r in range(rows):
        weights = []
        for c in range(rows):
            if c <= r:
                z = weight_on(r,c)
                weights.append(z)
        pprint(weights)
    end = timer()

    print(f"Elapsed time: {end-start} seconds")
    print(f"Number of function calls: {call_count}")
    print(f'Number of cache hits: {cache_hits}')

if __name__ == "__main__":
    main()
