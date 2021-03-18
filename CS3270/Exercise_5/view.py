import sys
import os
# [X] Get command line arguments
# [X] Get input from user to know where to naviage the page
# [] Implement commands [u,d,t,b,#,q]
# [] Enter is a down command
# [] Don't allow viewing empty files
# [] Read file in only the pre-determined amount, not the entire file

path = os.path.dirname(__file__)
view_size = 25
fname = path + '/yankee.txt'
#fname = sys.argv[1]

# This is optional, if I can't figure out how to make sure this variable exists, remove it all together
#view_size = sys.argv[2]

def view(args):
    #print(fname)
    #print(view_size)
    with open(fname, 'r') as f:
        print(f.seek(20))
            #x = input("Please enter something: ")
            #print(x)

if __name__ == '__main__':
    view(sys.argv)
