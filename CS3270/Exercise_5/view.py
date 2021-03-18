import sys
import os
# [X] Get command line arguments
# [X] Get input from user to know where to naviage the page
# [X] Get files offsets to sort pages accordingly
# [X] Read file in only the pre-determined amount, not the entire file
# [] Implement commands [u,d,t,b,#,q]
# [] Enter is a down command
# [] Don't allow viewing empty files

path = os.path.dirname(__file__)
view_size = 25
fname = path + '/yankee.txt'
#fname = sys.argv[1]

# This is optional, if I can't figure out how to make sure this variable exists, remove it all together
#view_size = sys.argv[2]


# How to pad the last lines of the file to make the view correct on the last page
# Need to figure out how to append the newline to the file, does doing a newline eat up a whole readline?
#while x % 25 != 0:
    #x += 1

def view(args):
    with open(fname, 'r') as f:
        # create list of offsets to use for naviagtion
        offsets = [0]
        cursor = (0)
        command = ''
        while f.readline():
            offsets.append(f.tell())
        offsets.pop()  # Remove EOF file POS
        # Print initial view
        for x in range(0, 20):
            f.seek(offsets[x])
            print(f.readline(), end='')
        cursor = offsets.index(f.tell())
        print('\n')
        print(len(offsets))
        while command != 'q':
            command = input('Command [u,d,t,b,#,q]: ')
            # Moves one page down; if at botton wrap to top
            if command == 'd':
                if cursor != offsets[-20]:
                    for x in range(cursor, cursor+20):
                        f.seek(offsets[x])
                        print(f.readline(), end='')
                    cursor = offsets.index(f.tell())
                else:
                    # Takes you to the first page if at the last page
                    for x in range(0, 20):
                        f.seek(offsets[x])
                        print(f.readline(), end='')
                    cursor = offsets.index(f.tell())

            if command == 'u':
                if cursor != offsets[0]:
                    for x in range(cursor - 20, cursor):
                        f.seek(offsets[x])
                        print(f.readline(), end='')
                    cursor = offsets.index(f.tell())
                else:
                    for x in range(offsets[-20], offsets[-1]):
                        f.seek(offsets[x])
                        print(f.readline(), end='')
                    cursor = offsets.index(f.tell())

            # Gets last index location for use with user input

        #x = input("Please enter something: ")
        # print(x)
if __name__ == '__main__':
    view(sys.argv)
