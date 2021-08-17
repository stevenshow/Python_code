def linear_search(my_list, target):
    for i in range(len(my_list)):
        if my_list[i] == target:
            return True
    return False

def binary_search(my_list, target):
    first = 0
    last = len(my_list) - 1
    found = False
    while first <= last and not found:
        mid = first + last // 2
        if target == my_list[mid]:
            found = True
        if target < my_list[mid]:
            last = mid - 1 
        else:
            first = mid + 1 
    return found

def jump_search(my_list, target):
    pass

# my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34]
# result = binary_search(my_list, my_list[-1])
# print(result)