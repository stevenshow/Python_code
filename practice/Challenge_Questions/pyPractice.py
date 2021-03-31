import math
from array import *
'''Question 6
Level 2

Question:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
'''

def squareRoot():
    h = 30
    c = 50
    q = []
    my_list = [x for x in input('Enter comma separated list of ints you would like to run through the equation: ').split(',')]
    for i in range(len(my_list)):
        q.append(round(math.sqrt((2 * c * int(my_list[i])/ h))))
    print(q)
#squareRoot()

'''Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], 
 [0, 1, 2, 3, 4], 
 [0, 2, 4, 6, 8]] 
'''

def create_2dArray(row, column):
    my_array = []

arr = [[0 for i in range(3)] for j in range(5)] 

#----------------------------------------#

#----------------------------------------#
'''Question 8
Level 2

Question:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

def word_sorter():
    word_list = [x for x in input('Enter comma separated list of words, and we will sort them for you: ').split(',')]
    #Removes all trailing and leading spaces from list
    word_list_no_space = [x.strip(' ') for x in word_list]
    word_list_no_space.sort()
    print(word_list_no_space)
word_sorter()

