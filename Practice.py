'''Question 1
Level 1

Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.'''

def question_1(div_by, not_mult_of):
    my_list = []
    for num in range(2000, 3201):
        if(num % div_by == 0 and num % not_mult_of != 0):
            my_list.append(str(num))
    print(my_list)
#question_1(7, 5)
#----------------------------------------#

#----------------------------------------#
'''Question 2
Level 1

Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
n! = n x (n-1)'''

def question2(num):
    if num == 0:
        return 1
    return num * question2(num - 1)
#print(question2(8))
#----------------------------------------#

#----------------------------------------#
'''Question:
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). 
and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}'''

def question3(num):
    my_dict = {}
    n = num
    for i in range(1, n + 1):
        my_dict[i] = i * i
    print(my_dict)
#question3(8)
#----------------------------------------#

#----------------------------------------#
'''Question 4
Level 1

Question:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')'''

def question4():
    numbers = input("Input a sequence of comma separated numbers like so '34,67,55,33,12,98' and it will be turned into a list and tuple: ")
    my_list = numbers.split(',')
    my_tuple = tuple(my_list)
    print(my_list)
    print(my_tuple)
#question4()
#----------------------------------------#

#----------------------------------------#
'''Question 5
Level 1

Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters'''

class InputOutString(object):
    def __init__(self):
        self.s = ""
    def getString(self):
        self.s = input('Please enter a string to be capitalized: ')
    def capitalizeString(self):
        print(self.s.upper())
#strObj = InputOutString()
#strObj.getString()
#strObj.capitalizeString() 
#----------------------------------------#

#----------------------------------------#
