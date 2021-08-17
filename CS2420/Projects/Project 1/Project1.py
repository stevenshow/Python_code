from random import seed, sample
from time import perf_counter
from math import sqrt
import time
from Searches import linear_search, binary_search, jump_search
import get_list


def first_element_search(my_list):
    start = time.perf_counter()
    result = linear_search(my_list, my_list[0])
    linear_end = time.perf_counter() - start
    assert result

    start = time.perf_counter()
    result = binary_search(my_list, my_list[0])
    binary_end = time.perf_counter() - start
    assert result

    # start = time.perf_counter()
    # result = jump_search(my_list, my_list[0])
    # jump_end = time.perf_counter() - start
    # assert result

    return (linear_end, binary_end)

def last_element(my_list, target):
    start = time.perf_counter()
    result = linear_search(my_list, target)
    linear_end = time.perf_counter() - start
    assert result

    start = time.perf_counter()
    result = binary_search(my_list, target)
    binary_end = time.perf_counter() - start
    assert result

    return linear_end, binary_end

def main():
    my_list = get_list.get_list(1000000)
    
    # first_ele = first_element_search(my_list)
    # print(first_ele)
    last_ele = last_element(my_list, my_list[-1])
    print(last_ele)

    



if __name__ == '__main__':
    main()
