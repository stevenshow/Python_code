'''
Question 1
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

