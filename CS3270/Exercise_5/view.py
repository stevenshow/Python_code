import sys
import os
# [X] Get input from user to know where to naviage the page
# [X] Get files offsets to sort pages accordingly
# [X] Read file in only the pre-determined amount, not the entire file
# [X] Implement commands [u,d,t,b,#,q]
# [X] d command
# [X] u command
# [X] t command
# [X] b command
# [X] # command
# [X] Enter is a down command
# [] Get command line arguments for file reading and view size
# [] Don't allow viewing empty files

path = os.path.dirname(__file__)
view_size = 20
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
        # while len(offsets) % 20 != 0:
        #     offsets.append('\n')
        #     f.write('\n')

        # Print initial view
        print(f'[Page {current_page + 1}]:')
        for x in range(0, view_size):
            f.seek(offsets[x])
            print(f.readline(), end='')
        print('\n')

        # Gets list of pages with their respectice indicies
        start = 0
        stop = view_size
        for x in range(int(len(offsets)/view_size)):
            pages.append(offsets[start:stop])
            start += view_size
            stop += view_size
        current_page = 1

        # Start loop to get and process input
        while command != 'q':
            command = input('Command [u,d,t,b,#,q]: ')
            
            # Moves one page down; if at botton wrap to the top
            if command == 'd' or command == '':
                if current_page <= len(pages) - 1:
                    current_page += 1
                    print(f'[Page {current_page}]:', current_page)
                    for x in range(len(pages[current_page-1])):
                        f.seek(pages[current_page-1][x])
                        print(f.readline(), end='')
                    print('\n')
                # If the current page is the last page
                #current_page should exit on 0
                else:
                    current_page = 1
                    print(f'[Page {current_page}]:', current_page)
                    for x in range(len(pages[current_page-1])):
                        f.seek(pages[current_page-1][x])
                        print(f.readline(), end='')
                    print('\n')
                    #current_page = 1
            
            # Moves view up 1 page; If at the top, wrap to the bottom
            if command == 'u':
                if current_page != 0 and current_page != 1:
                    current_page -= 1
                    print(f'[Page {current_page}]:', current_page)
                    for x in range(len(pages[current_page-1])):
                        f.seek(pages[current_page-1][x])
                        print(f.readline(), end='')
                    print('\n')
                # If the current page is the first page
                # current_page should exit on 100
                else:
                    current_page = len(pages)
                    print(f'[Page {current_page}]:', current_page)
                    for x in range(len(pages[-1])):
                        f.seek(pages[-1][x])
                        print(f.readline(), end='')
                    print('\n')
                    current_page = len(pages)
            
            # Moves to the top page
            if command == 't':
                current_page = 1
                print(f'[Page {current_page}]:', current_page)
                for x in range(len(pages[current_page-1])):
                    f.seek(pages[current_page-1][x])
                    print(f.readline(), end='')
                print('\n')

            # Moved to the bottom page
            if command == 'b':
                current_page = len(pages)
                print(f'[Page {current_page}]:', current_page)
                for x in range(len(pages[-1])):
                    f.seek(pages[-1][x])
                    print(f.readline(), end='')
                print('\n')
                current_page = len(pages)

            # Move to the specified page number
            if command.isdigit() and int(command) <= len(pages) and int(command) > 0:
                current_page = int(command)
                print(f'[Page {current_page}]:', current_page)
                for x in range(len(pages[current_page-1])):
                    f.seek(pages[current_page-1][x])
                    print(f.readline(), end='')
                print('\n')


if __name__ == '__main__':
    view(sys.argv)
