'''Extracts from a zip file all the files whose basename match the regex argument
passed on the command lines
Created by: Steven Schoebinger'''
import os
import re
import sqlite3
import sys
from zipfile import ZipFile


def main():
    py_path = os.path.dirname(os.path.abspath(sys.argv[0])) + '/'
    count = 0
    with ZipFile(py_path + f'{sys.argv[1]}', 'r') as file:
        for f in file.namelist():
            fname = f.split('/')
            if re.search(f'{sys.argv[2]}', fname[-1]):
                count +=1
                file.extract(f, 'Stuff_Extracted')
        print(str(count) + ' files extracted')


if __name__ == '__main__':
    main()
