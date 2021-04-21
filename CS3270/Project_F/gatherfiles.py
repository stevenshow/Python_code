import sys
import os
import sqlite3
from zipfile import ZipFile
# Get all arguments after the .py file passed and database
for arg in sys.argv[2:]:
    print(arg)

def main():

    connection = sqlite3.connect(sys.argv[1])
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM files WHERE ext = 'cpp'")
    cpp_files = cursor.fetchall()
    print(len(cpp_files))
    cursor.execute("SELECT * FROM files WHERE ext = 'py'")
    py_files = cursor.fetchall()
    print(len(py_files))
    connection.close()

    with ZipFile('cpp.zip', 'w') as cppZip:
        for file in cpp_files:
            print(os.path.join(file[1], file[2]))

if __name__ == main():
    main()