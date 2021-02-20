from itertools import islice

the_string = 'A2B5E3426FG0ZYW3210PQ89R'

def produce(my_string):
    how_many = 0
    last_was_digit = False
    for x in my_string:
        if x.isdigit() and last_was_digit == False:
            how_many = int(x) + 1
            last_was_digit = True
        elif last_was_digit:
            yield x * how_many
            last_was_digit = False
        else:
            yield x

def consume1(my_iter):
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

#p = produce(the_string)
#for s in p: print(s,end=' ')


#def consume(my_iter):
#    characters = ''
#    count = 0
#    for x in my_iter:
#        if len(x) < 3:
#            characters = x
#        if len(characters) == 3:
#            print(characters)
#            characters = 0
#        if len(x) == 3:
#            print(x)
#        elif len(x) > 3:
#            print(x[0:3])
#            characters = x[3:]