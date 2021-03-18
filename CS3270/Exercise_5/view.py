import sys
# [X] Get command line arguments
# [X] Get input from user to know where to naviage the page
# [] Implement commands [u,d,t,b,#,q]
# [] Enter is a down command
# [] Don't allow viewing empty files
# [] Read file in only the pre-determined amount, not the entire file
view_size = 25
fname = sys.argv[1]
# This is optional, if I can't figure out how to make sure this variable exists, remove it all together
view_size = sys.argv[2]


def view(fname, view_size=25):
    print(fname)
    print(view_size)
    while True:
        x = input("Please enter something: ")
        print(x)
    # print(fname)


view(fname, view_size)
