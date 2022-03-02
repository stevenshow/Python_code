'''
Project: CS 2420 Fall 2020 Search Project (Project 1) Instructor Solution
Author: George Rudolph
Date: 4 Dec 2020
'''

from random import seed, sample
from time import perf_counter
from math import sqrt

def linear_search(lyst, target):
    ''' sequencially searches elements of lyst to find target. 
    '''
    for x in lyst:
        if target == x:
            return True
    return False

def binary_search(lyst, target):
    ''' binary searches elements of lyst to find target. 
        lyst MUST be sorted (assending)
        Returns True if found, else returns False.
    '''
    if not lyst:
        return False
    
    low = 0
    high = len(lyst) - 1
    
    while True:
        if low > high:
            return False
        mid = (low + high) // 2
        if lyst[mid] == target:
            return True
        if target < lyst[mid]:
            high = mid - 1
        else:
            low = mid + 1
            
def jump_search(lyst, target):
    ''' jump searches elements of lyst to find target. 
        lyst MUST be sorted (ascending)
        Returns True if found, else returns False.
    '''
    step = int(sqrt(len(lyst)))

    # find the block where target is present
    previous = 0
    next = previous + step
    while next < len(lyst) and lyst[next] < target:
        previous = next
        next = previous + step

    # search sequencially from previous to next for target
    for i in range(previous, min(next, len(lyst))):
        if lyst[i] == target:
            return True
    return False

def main():
    ''' non-interactive function which creates a sorted
    data list and then exercises all three searching functions '''
    DATA_SIZE = 10000000
    seed(0)
    print(f"Creating a sorted array of {DATA_SIZE}")
    data = sample(range(DATA_SIZE * 3), k=DATA_SIZE)
    print("sorting")
    data.sort()
    print(f"Finished creating a sorted array of {DATA_SIZE}")
    print()

    where = {
        0: "at the start",
        -1: "at the end",
        (DATA_SIZE -1)//2: "in the middle"
        }
    for k, v in where.items():
        print()
        print(f"Searching for a number {v} of the array")
        for f in [linear_search, binary_search, jump_search]:
            start = perf_counter()
            result = f(data, data[k])
            elapsed_time = perf_counter() - start
            print(f"\t{f.__name__} returned {result} in {elapsed_time:e} seconds")
    
'''

    print("Searching for a number in the middle of the array")
    start = perf_counter()
    result = linear_search(data, data[(DATA_SIZE - 1) // 2])
    elapsed_time = perf_counter() - start
    print("\tlinear_search() returned", result, "in", f"{elapsed_time:.7f} seconds")
    start = perf_counter()
    result = recursive_binary_search(data, data[(DATA_SIZE - 1) // 2])
    elapsed_time = perf_counter() - start
    print("\trecursive_binary_search() returned", result, "in", f"{elapsed_time:.7f} seconds")
    start = perf_counter()
    result = jump_search(data, data[(DATA_SIZE - 1) // 2])
    elapsed_time = perf_counter() - start
    print("\tjump_search() returned", result, "in", f"{elapsed_time:.7f} seconds")

    print("Searching for a number at the end of the array")
    start = perf_counter()
    result = linear_search(data, data[DATA_SIZE - 1])
    elapsed_time = perf_counter() - start
    print("\tlinear_search() returned", result, "in", f"{elapsed_time:.7f} seconds")
    start = perf_counter()
    result = recursive_binary_search(data, data[DATA_SIZE - 1])
    elapsed_time = perf_counter() - start
    print("\trecursive_binary_search() returned", result, "in", f"{elapsed_time:.7f} seconds")
    start = perf_counter()
    result = jump_search(data, data[DATA_SIZE - 1])
    elapsed_time = perf_counter() - start
    print("\tjump_search() returned", result, "in", f"{elapsed_time:.7f} seconds")

    print("Searching for a number NOT in the array")
    start = perf_counter()
    result = linear_search(data, -1)
    elapsed_time = perf_counter() - start
    print("\tlinear_search() returned", result, "in", f"{elapsed_time:.7f} seconds")
    start = perf_counter()
    result = recursive_binary_search(data, -1)
    elapsed_time = perf_counter() - start
    print("\trecursive_binary_search() returned", result, "in", f"{elapsed_time:.7f} seconds")
    start = perf_counter()
    result = jump_search(data, -1)
    elapsed_time = perf_counter() - start
    print("\tjump_search() returned", result, "in", f"{elapsed_time:.7f} seconds")
'''

if __name__ == "__main__":
    main()