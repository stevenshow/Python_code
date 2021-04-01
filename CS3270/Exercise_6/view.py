'''Command line program that takes a file name and a view size
and then outputs the file 1 page at a time based on the view size
Created by: Steven Schoebinger 03/19/2021'''
import math
import os
import sys
from tkinter import *
import tkinter.simpledialog as simpledialog
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
current_page = 0
# If a command line argument is passed
if len(sys.argv) > 1:
    fname = path + sys.argv[1]
    try:
        view_size = int(sys.argv[2])
    # If there is no view size passed
    except IndexError:
        view_size = 20


def down(f, t, root, pages):
    '''Moves one page down; if at botton wrap to the top; returns current page after print'''
    global current_page
    if current_page <= len(pages) - 1:
        current_page += 1
        t.config(state=NORMAL)
        t.delete('1.0', END)
        for x in range(len(pages[current_page-1])):
            f.seek(pages[current_page-1][x])
            t.insert(END, f.readline())
        root.title('yankee.txt - Page ' + str(current_page))
    # If the current page is the last page
    else:
        current_page = 1
        t.config(state=NORMAL)
        t.delete('1.0', END)
        for x in range(len(pages[current_page-1])):
            f.seek(pages[current_page-1][x])
            t.insert(END, f.readline())
        root.title('yankee.txt - Page ' + str(current_page))
    return current_page


def up(f, t, root, pages):
    '''Moves up one page; if at top wrap to the bottom; returns current page after print'''
    global current_page
    if current_page not in [0, 1]:
        current_page -= 1
        t.config(state=NORMAL)
        t.delete('1.0', END)
        for x in range(len(pages[current_page-1])):
            f.seek(pages[current_page-1][x])
            t.insert(END, f.readline())
        root.title('yankee.txt - Page ' + str(current_page))
    # If the current page is the first page
    else:
        current_page = len(pages)
        t.config(state=NORMAL)
        t.delete('1.0', END)
        for x in range(len(pages[-1])):
            f.seek(pages[-1][x])
            t.insert(END, f.readline())
        root.title('yankee.txt - Page ' + str(current_page))

def top(f, t, root, pages):
    '''Moves to the top page; returns current page after print'''
    global current_page
    current_page = 1
    t.config(state=NORMAL)
    t.delete('1.0', END)
    for x in range(len(pages[current_page-1])):
        f.seek(pages[current_page-1][x])
        t.insert(END, f.readline())
    root.title('yankee.txt - Page ' + str(current_page))

def bottom(f, t, root, pages):
    '''Moves to the bottom page; returns current page after print'''
    global current_page
    current_page = len(pages)
    t.config(state=NORMAL)
    t.delete('1.0', END)
    for x in range(len(pages[-1])):
        f.seek(pages[-1][x])
        t.insert(END, f.readline())
    root.title('yankee.txt - Page ' + str(current_page))

def to_page(f, t, root, pages):
    '''Moves to the page passed by user; returns current page after print'''
    global current_page
    current_page = int(simpledialog.askinteger("Page Number", "Enter page number"))
    while current_page > 100 or current_page < 0:
        current_page = int(simpledialog.askinteger("Page Number", "Enter page number"))
    if current_page == 0:
        current_page = 1
    t.config(state=NORMAL)
    t.delete('1.0', END)
    for x in range(len(pages[current_page-1])):
        f.seek(pages[current_page-1][x])
        t.insert(END, f.readline())
    root.title('yankee.txt - Page ' + str(current_page))
    

def text_gui(file, pages, size, offsets):
    # [X] Create display window
    # [X] Create all buttons and link them to functions
    # [X] Create Horizontal scrollbar
    # [X] Receive input from user for page jumping
    # [X] Display correct page without wrapping

    global current_page
    with open(file, 'r+') as f:
        root = Tk()
        toolbar = Frame(root)
        # Creation of all buttons
        t = Text(root, height=20, width=50, wrap='none')
        top_b = Button(toolbar, text='Top', command=lambda: top(f, t, root, pages), padx='5', pady='5')
        up_b = Button(toolbar, text='Up', command=lambda: up(f, t, root, pages), padx='5', pady='5')
        down_b = Button(toolbar, text='Down', command=lambda: down(f, t, root, pages), padx='5', pady='5')
        bottom_b = Button(toolbar, text='Bottom', command=lambda: bottom(f, t, root, pages), padx='5', pady='5')
        # Get user response for page number
        page_b = Button(toolbar, text='Page', command=lambda: to_page(f, t, root, pages), padx='5', pady='5')
        b_quit = Button(toolbar, text='Quit', fg='red', command=quit)

        # Start loop to get and process input           
        # Trying to place in center of screen
        windowWidth = root.winfo_reqwidth()
        windowHeight = root.winfo_reqheight()
        posRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
        posDown = int(root.winfo_screenmmheight() - windowHeight/2)
        
        # Horizontal Scrollbar
        t.pack()
        scrollbar = Scrollbar(root, orient='horizontal')
        scrollbar.pack(side=BOTTOM, fill=X)
        t.config(xscrollcommand=scrollbar.set)
        scrollbar.config(command=t.xview)
        
        # All buttons and main window
        toolbar.pack()
        top_b.pack(side=LEFT)
        up_b.pack(side=LEFT)
        down_b.pack(side=LEFT)
        bottom_b.pack(side=LEFT)
        page_b.pack(side=LEFT)
        b_quit.pack(side=LEFT)
        root.title('yankee.txt - Page ' + str(current_page))
        root.geometry("400x400+{}+{}".format(posRight, posDown))
        # Print initial view
        for x in range(0, size):
            f.seek(offsets[x])
            t.insert(END, f.readline())
        root.mainloop()


def view(file, size):
    '''Finds the line offsets of the file and then places them in a list.
    Uses that list to create pages based on view_size'''
    # Checks if the file is empty
    global current_page
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

        text_gui(file, pages, size, offsets)

    else:
        print('File is empty!')
        sys.exit()


if __name__ == '__main__':
    view(fname, view_size)
