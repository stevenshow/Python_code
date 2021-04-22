'''Extracts from a zip file all the files whose basename match the regex argument
passed on the command lines
Created by: Steven Schoebinger 04/21/2021'''
import os
import re
import sys
from zipfile import ZipFile

# pylint: disable=invalid-name


def main():
    '''Extracts from a zip file all the files whose basename match the regex argument
    passed on the command lines'''
    py_path = os.path.dirname(os.path.abspath(sys.argv[0])) + '/'
    count = 0
    with ZipFile(py_path + f'{sys.argv[1]}', 'r') as file:
        for f in file.namelist():
            fname = f.split('/')
            if re.search(f'{sys.argv[2]}', fname[-1]):
                count += 1
                file.extract(f, 'part3')
        print(str(count) + ' files extracted')


if __name__ == '__main__':
    main()
