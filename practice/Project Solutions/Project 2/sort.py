'''
Project Name: Project 2: Sort
Author: George Rudolph
Course: CS 2420-002
Due Date: 4 Jul 2020

This is my example instructor solution for Project 2.
Students will not do everything quite the way I do it, but that's OK.
I used restructured text to format my function docstrings.
'''

from random import seed, sample
import time

def quicksort(lyst, counter=None):
    ''' This quicksort sorts a copy of the list, so the original list remains.

    :parameter lyst: a list of any comaprable type, such as int.
    :parameter target: the value to search for.
    :parameter counter: an optional generator to count levels of recursion.
    :return: A copy of the list is sorted order.
    :rtype: list
    '''
    if counter:
        next(counter)

    if not isinstance(lyst, list):
        raise ValueError("Parameter is not a list.")

    if not lyst:
        return []
    if len(lyst) == 1:
        return lyst[:]
    if len(lyst) == 2:
        lyst.sort()
        return lyst[:]

    pivot = lyst[-1]
    left = []
    right = []
    for value in lyst[:-1]:
        if value < pivot:
            left.append(value)
        else:
            right.append(value)
    return quicksort(left) + [pivot] + quicksort(right)

def selection_sort(lyst):
    ''' Implement selection sort on a copy of the list so the original remains unchanged.

    :parameter lyst: a list of any comaprable type, such as int.
    :parameter target: the value to search for.
    :return: True id target value is found, False otherwise.
    :rtype: boolean

    .. warning::
        destroys the input list.
    '''
    if not isinstance(lyst, list):
        raise ValueError("Parameter is not a list.")

    if not lyst:
        return []
    if len(lyst) == 1:
        return lyst[:]
    if len(lyst) == 2:
        lyst.sort()
        return lyst[:]

    sorted_lyst = []
    while lyst:
        idx_of_min = 0
        for idx, value in enumerate(lyst):
            if value < lyst[idx_of_min]:
                idx_of_min = idx
        value = lyst.pop(idx_of_min)
        sorted_lyst.append(value)

    return sorted_lyst

def insertion_sort(lyst):
    ''' Do jump search of a list for target value.

    :parameter lyst: a list of any comaprable type, such as int.
    :parameter target: the value to search for.
    :return: True id target value is found, False otherwise.
    :rtype: boolean
    '''
    if not isinstance(lyst, list):
        raise ValueError("Parameter is not a list.")

    if not lyst:
        return []
    if len(lyst) == 1:
        return lyst[:]
    if len(lyst) == 2:
        lyst.sort()
        return lyst[:]

    sorted_lyst = [lyst[0]]
    for value in lyst[1:]:
        pos = 0
        while pos < len(sorted_lyst) and sorted_lyst[pos] < value:
            pos += 1
        if pos < len(sorted_lyst):
            sorted_lyst.insert(pos, value)
        else:
            lyst.append(value)
    return sorted_lyst

def mergesort(lyst, counter=None):
    ''' This mergesort sorts a copy of the list, so the original list remains.

    :parameter lyst: a list of any comaprable type, such as int.
    :parameter target: the value to search for.
    :parameter counter: an optional generator to count levels of recursion.
    :return: A copy of the list is sorted order.
    :rtype: list
    '''
    def merge(left, right):
        ''' Helper function to merge two sorted lists. '''
        merged_lyst = []
        while left and right:
            if left[0] > right[0]:
                value = right.pop(0)
            else:
                value = left.pop(0)
            merged_lyst.append(value)
        while left:
            value = left.pop(0)
            merged_lyst.append(value)
        while right:
            value = right.pop(0)
            merged_lyst.append(value)
        return merged_lyst
        # end helper function

    if not isinstance(lyst, list):
        raise ValueError("Parameter is not a list.")

    # this line of code instruments this function to count recursion.
    # if there is no counter, nothing happens.
    if counter:
        next(counter)

    if not lyst:
        return []
    if len(lyst) == 1:
        return lyst[:]
    if len(lyst) == 2:
        lyst.sort()
        return lyst[:]

    left = lyst[:len(lyst)//2]
    right = lyst[len(lyst)//2:]
    left = mergesort(left)
    right = mergesort(right)
    return merge(left, right)

def is_sorted(lyst):
    ''' Predicate determines if a list is sorted or not.

    :parameter lyst: a list of any comparable type, such as int.
    :return: True if list is sorted, False otherwise.
    :rtype: boolean
    '''
    if not isinstance(lyst, list):
        raise ValueError("Parameter is not a list.")

    invalid_type = any(not isinstance(value, int) for value in lyst)
    if invalid_type:
        raise ValueError("At least one item in the list is not an integer.")

    for pos in range(len(lyst)-1):
        if lyst[pos] > lyst[pos+1]:
            return False
    return True

def main():
    '''  This code is for benchmarking each of the sort routines as
    described in the project document.

    Here benchmarking means that we calculate the elapsed time for
    each sort routine on the same list, probing for the 1st element,
    middle element, last element and a target not in the list.
    Our implementations show that practice confirms theory for
    expected behavior of these algorithms.
    '''
    size = 10000
    print(f"Creating a sorted array of {size}")
    seed(0)
    data = sample(range(size*3), k=size)

    labels = ['selection_sort', 'insertion_sort',
              'mergesort', 'quicksort', 'timsort']
    sorts = [selection_sort, insertion_sort, mergesort, quicksort, sorted]
    for label, sort_routine in zip(labels, sorts):
        dup = data.copy()
        print(f"starting {label}")
        start = time.perf_counter()
        sort_routine(dup)
        duration = time.perf_counter() - start
        print(f"{label} duration: {duration} seconds.\n")

if __name__ == "__main__":
    main()
