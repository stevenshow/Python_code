# Return the sum of the numbers in the array, returning 0 for an empty array.
# Except the number 13 is very unlucky, so it does not count and numbers that
# come immediately after a 13 also do not count.

# sum13([1, 2, 2, 1]) → 6
# sum13([1, 1]) → 2
# sum13([1, 2, 2, 1, 13]) → 6
def sum13(nums):
    sum = 0
    skip = False
    if(len(nums) < 1):
        return 0
    else:
        for i in nums:
            if(i == 13):
                skip = True
                continue
            if(skip):
                skip = False
                continue
            else:
                sum += i
        return sum


def main():
    print(sum13([1, 2, 2, 1]))
    print(sum13([1, 1]))
    print(sum13([1, 2, 13, 2, 1, 13]))


if __name__ == '__main__':
    main()
