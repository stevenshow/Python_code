'''Takes command line arguments for database and extensions
    Takes extension and searches database for all files with the extension
    and places them in a zip file {ext}.zip
    Created by: Steven Schoebinger 04/21/2021'''
import os
import sqlite3
import sys
from zipfile import ZipFile

def main():
    '''Takes command line arguments for database and extensions
    Takes extension and searches database for all files with the extension
    and places them in a zip file {ext}.zip'''
    path = os.path.dirname(os.path.abspath(sys.argv[0])) + '/'
    connection = sqlite3.connect(sys.argv[1])
    cursor = connection.cursor()
    for arg in sys.argv[2:]:
        cursor.execute(f"SELECT * FROM files WHERE ext = '{arg}'")
        files = cursor.fetchall()
        if os.path.exists(path + f'{arg}.zip'):
            os.remove(path + f'{arg}.zip')
        with ZipFile(f'{arg}.zip', 'w') as cppZip:
            for file in files:
                cppZip.write(os.path.join(file[1], file[2]))
            print(str(len(files)) + f' {arg} files gathered')

if __name__ == main():
    main()
