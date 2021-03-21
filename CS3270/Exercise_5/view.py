'''Command line program that takes a file name and a view size
and then outputs the file 1 page at a time based on the view size
Created by: Steven Schoebinger 03/19/2021'''
import sys
import os
import math
# pylint: disable=invalid-name
# [X] Get input from user to know where to naviage the page
# [X] Get files offsets to sort pages accordingly
# [X] Read file in only the pre-determined amount, not the entire file
# [X] Implement commands [u,d,t,b,#,q]; Enter is a down command
# [X] Get command line arguments for file reading and view size
# [X] Don't allow viewing empty files

# Gets directory name in either IDE or Command Line; Sets defaults if nothing is passed
path = os.path.dirname(os.path.abspath(sys.argv[0])) + '/'
fname = path + 'yankee.txt'
view_size = 20

# If a command line argument is passed
if len(sys.argv) > 1:
    fname = path + sys.argv[1]
    try:
        view_size = int(sys.argv[2])
    # If there is no view size passed
    except IndexError:
        view_size = 20

def down(f, current_page, pages):
    '''Moves one page down; if at botton wrap to the top; returns current page after print'''
    if current_page <= len(pages) - 1:
        current_page += 1
        print(f'[Page {current_page}]:')
        for x in range(len(pages[current_page-1])):
            f.seek(pages[current_page-1][x])
            print(f.readline(), end='')
        print('\n')
    # If the current page is the last page
    else:
        current_page = 1
        print(f'[Page {current_page}]:')
        for x in range(len(pages[current_page-1])):
            f.seek(pages[current_page-1][x])
            print(f.readline(), end='')
        print('\n')
    return current_page

def up(f, current_page, pages):
    '''Moves up one page; if at top wrap to the bottom; returns current page after print'''
    if current_page not in [0,1]:
        current_page -= 1
        print(f'[Page {current_page}]:')
        for x in range(len(pages[current_page-1])):
            f.seek(pages[current_page-1][x])
            print(f.readline(), end='')
        print('\n')
    # If the current page is the first page
    else:
        current_page = len(pages)
        print(f'[Page {current_page}]:')
        for x in range(len(pages[-1])):
            f.seek(pages[-1][x])
            print(f.readline(), end='')
        print('\n')
        current_page = len(pages)
    return current_page

def top(f, current_page, pages):
    '''Moves to the top page; returns current page after print'''
    current_page = 1
    print(f'[Page {current_page}]:')
    for x in range(len(pages[current_page-1])):
        f.seek(pages[current_page-1][x])
        print(f.readline(), end='')
    print('\n')
    return current_page

def bottom(f, current_page, pages):
    '''Moves to the bottom page; returns current page after print'''
    current_page = len(pages)
    print(f'[Page {current_page}]:')
    for x in range(len(pages[-1])):
        f.seek(pages[-1][x])
        print(f.readline(), end='')
    print('\n')
    current_page = len(pages)
    return current_page

def to_page(f, current_page, pages, command):
    '''Moves to the page passed by user; returns current page after print'''
    current_page = int(command)
    print(f'[Page {current_page}]:')
    for x in range(len(pages[current_page-1])):
        f.seek(pages[current_page-1][x])
        print(f.readline(), end='')
    print('\n')
    return current_page

def view(file, size):
    '''Finds the line offsets of the file and then places them in a list.
    Uses that list to create pages based on view_size'''
    # Checks if the file is empty
    if os.path.getsize(file) != 0:
        with open(file, 'r+') as f:
            # create list of offsets to use for naviagtion
            current_page = 0
            offsets = [0]
            command = ''
            pages = []

            # Gets list of line offsets
            while f.readline():
                offsets.append(f.tell())
            f.seek(offsets.pop())
            print(f.readline(), end='')

            # Print initial view
            print(f'[Page {current_page+1}]:')
            for x in range(0, size):
                f.seek(offsets[x])
                print(f.readline(), end='')
            print('\n')

            # Gets list of pages with their respective indicies
            start = 0
            stop = size
            for x in range(math.ceil(len(offsets)/size)):
                pages.append(offsets[start:stop])
                start += size
                stop += size
            current_page = 1

            # Start loop to get and process input
            while command != 'q':
                command = input('Command [u,d,t,b,#,q]: ')
                # Moves one page down; if at botton wrap to the top
                if command in ['', 'd']:
                    current_page = down(f, current_page, pages)
                # Moves view up 1 page; If at the top, wrap to the bottom
                if command == 'u':
                    current_page = up(f,current_page, pages)
                # Moves to the top page
                if command == 't':
                    current_page = top(f, current_page, pages)
                # Moves to the bottom page
                if command == 'b':
                    current_page = bottom(f, current_page, pages)
                # Move to the specified page number
                if command.isdigit() and int(command) <= len(pages) and int(command) > 0:
                    current_page = to_page(f, current_page, pages, command)
    else:
        print('File is empty!')
        sys.exit()

if __name__ == '__main__':
    view(fname, view_size)
