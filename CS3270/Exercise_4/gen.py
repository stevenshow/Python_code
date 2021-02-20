'''Uses generators to process a string a character at a time and
return a string based on pre-set conditions with digits.
Created by: Steven Schoebinger 2/19/2021'''
# pylint: disable=invalid-name

the_string = 'A2B5E3426FG0ZYW3210PQ89R'

def produce(my_string):
    '''Processes the string and yields to new string'''
    how_many = 0
    last_was_digit = False
    for x in my_string:
        if x.isdigit() and not last_was_digit:
            how_many = int(x) + 1
            last_was_digit = True
        elif last_was_digit:
            yield x * how_many
            last_was_digit = False
        else:
            yield x

def consume1(my_iter):
    '''Grabs the processed generator stream and prints groups of 3'''
    stream = []
    #while my_iter:
    for x in my_iter:
        for char in x:
            if len(stream) < 3:
                stream.append(char)
            elif len(stream) == 3:
                print(''.join(stream), end=' ')
                stream.clear()
                stream.append(char)
    print(''.join(stream))

consume1(produce(the_string))
