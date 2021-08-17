from random import seed, sample
from time import perf_counter
from math import sqrt
import time
from Searches import linear_search, binary_search, jump_search
import get_list


def first_element_search(my_list):
    print(linear_search(my_list, my_list[0]))


def main():
    my_list = get_list.get_list(100000)
    first_element_search(my_list)



if __name__ == '__main__':
    main()
