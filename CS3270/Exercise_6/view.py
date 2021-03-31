'''Command line program that takes a file name and a view size
and then outputs the file 1 page at a time based on the view size
Created by: Steven Schoebinger 03/19/2021'''
import math
import os
import sys
from tkinter import *
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


def up(f, t, current_page, pages):
    '''Moves up one page; if at top wrap to the bottom; returns current page after print'''
    print(current_page)
    if current_page not in [0, 1]:
        current_page -= 1
        print(f'[Page {current_page}]:')
        t.config(state=NORMAL)
        t.delete('0.0', END)
        for x in range(len(pages[current_page-1])):
            f.seek(pages[current_page-1][x])
            t.insert(END, f.readline())
        #print('\n')
    # If the current page is the first page
    else:
        current_page = len(pages)
        print(f'[Page {current_page}]:')
        t.config(state=NORMAL)
        t.delete('0.0', END)
        for x in range(len(pages[-1])):
            f.seek(pages[-1][x])
            t.insert(END, f.readline())
        #print('\n')
        current_page = len(pages)
    print(current_page)
    return current_page


def top(f, t, current_page, pages):
    '''Moves to the top page; returns current page after print'''
    current_page = 1
    print(f'[Page {current_page}]:')
    t.config(state=NORMAL)
    t.delete('0.0', END)
    for x in range(len(pages[current_page-1])):
        f.seek(pages[current_page-1][x])
        t.insert(END, f.readline())
    #print('\n')
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
        t.insert(END, f.readline())
    print('\n')
    return current_page

def text_gui(file, current_page, pages):
    # Create display window
    with open(file, 'r+') as f:
        root = Tk()
        toolbar = Frame(root)

        b_quit = Button(toolbar, text='Quit', fg='red', command=quit)
        print('this ', current_page)
        t = Text(root, height=20, width=50)
        b = Button(toolbar, text='Top', command=lambda: top(f, t, current_page, pages), padx='5', pady='5')
        r = Button(toolbar, text='Up', command=lambda: up(f, t, current_page, pages), padx='5', pady='5')
        # Start loop to get and process input           

        # Trying to place in center of screen
        windowWidth = root.winfo_reqwidth()
        windowHeight = root.winfo_reqheight()
        posRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
        posDown = int(root.winfo_screenmmheight() - windowHeight/2)

        t.pack()
        toolbar.pack()
        r.pack(side=LEFT)
        b.pack(side=LEFT)
        b_quit.pack(side=RIGHT)
        root.title('Window')
        root.geometry("300x300+{}+{}".format(posRight, posDown))
        root.mainloop()


def view(file, size):
    '''Finds the line offsets of the file and then places them in a list.
    Uses that list to create pages based on view_size'''
    # Checks if the file is empty
    if os.path.getsize(file) != 0:
        with open(file, 'r+') as f:
            # create list of offsets to use for naviagtion
            current_page = 0
            offsets = [0]
            pages = []

            # Gets list of line offsets
            while f.readline():
                offsets.append(f.tell())
            f.seek(offsets.pop())
            print(f.readline(), end='')

            # Gets list of pages with their respective indicies
            start = 0
            stop = size
            for _ in range(math.ceil(len(offsets)/size)):
                pages.append(offsets[start:stop])
                start += size
                stop += size
            current_page = 1

            text_gui(file, current_page, pages)


            

    else:
        print('File is empty!')
        sys.exit()




if __name__ == '__main__':
    view(fname, view_size)
