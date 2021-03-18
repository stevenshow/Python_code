import sys
import os
# [X] Get command line arguments
# [X] Get input from user to know where to naviage the page
# [X] Get files offsets to sort pages accordingly
# [X] Read file in only the pre-determined amount, not the entire file
# [] Implement commands [u,d,t,b,#,q]
# [X] d command
# [X] u command
# [] t command
# [] b command
# [] # command
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
# while x % 25 != 0:
#x += 1

def view(args):
    with open(fname, 'r+') as f:
        # create list of offsets to use for naviagtion
        current_page = 0
        offsets = [0]
        command = ''
        pages = []
        
        while f.readline():
            offsets.append(f.tell())
        offsets.pop()  # Remove EOF file POS
        f.seek(offsets.pop())
        print(f.readline(), end='')
        
        # Add newlines until the offsets mod viewsize = 0 so the views are all equal
        while len(offsets) % 20 != 0:
            offsets.append('\n')
            f.write('\n')
        
        # Print initial view
        for x in range(0, 20):
            f.seek(offsets[x])
            print(f.readline(), end='')
        print('\n')
        
        # Gets list of pages with their respectice indicies
        start = 0
        stop = 20
        for x in range(int(len(offsets)/20)):    
            pages.append(offsets[start:stop])
            start += 20
            stop += 20

        while command != 'q':
            command = input('Command [u,d,t,b,#,q]: ')
            # Moves one page down; if at botton wrap to top
            if command == 'd':
                if current_page != len(pages) - 1:
                    for x in range(len(pages[current_page+1])):
                        f.seek(pages[current_page+1][x])
                        print(f.readline(), end='')
                    current_page += 1
                else:
                    for x in range(len(pages[0])):
                        f.seek(pages[0][x])
                        print(f.readline(), end='')
                    current_page = 0

            if command == 'u':
                if current_page != 0:
                    for x in range(len(pages[current_page-1])):
                        f.seek(pages[current_page-1][x])
                        print(f.readline(), end='')
                    current_page -= 1
                else:
                    for x in range(len(pages[-1])):
                        f.seek(pages[-1][x])
                        print(f.readline(), end='')
                    current_page = len(pages) - 1
                
            if command == 't':

            # Gets last index location for use with user input

        #x = input("Please enter something: ")
        # print(x)
if __name__ == '__main__':
    view(sys.argv)
