'''Script that takes a command line argument of the directory name that you would like
to traverse and store each file in the created database.
Created by: Steven Schoebinger 04/20/2021'''
import os
import sqlite3
import sys

# pylint: disable=invalid-name


def main():
    '''Script that takes a command line argument of the directory name that you would like
    to traverse and store each file in the created database.'''
    py_path = os.path.dirname(os.path.abspath(sys.argv[0])) + '/'
    path = os.path.dirname(os.path.abspath(sys.argv[0])) + '/' + sys.argv[1]
    db_path = os.path.join(py_path, 'filesdb.sqlite3')
    # Create new database each time so the data is always correct
    if os.path.exists(db_path):
        os.remove(db_path)

    connection = sqlite3.connect(db_path)
    print('filesdb created')
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE files (
                ext TEXT,
                path TEXT,
                fname TEXT
                )''')

    # os.walk will go through each directory and collect all files
    for root, _, files in os.walk(path):
        # root will get the path to the files
        print('entered loop')
        for file in files:
            if file.split('.')[0] == '_' or file.split('.')[0] == '':
                break
            if len(file.split('.')) > 1:
                fname = file
                print(fname)
                ext = file.split('.')[1]
                path = root
                cursor.execute(
                    'INSERT INTO files VALUES (?,?,?)', (ext, path, fname))
            else:
                fname = file
                ext = None
                path = root
                cursor.execute(
                    'INSERT INTO files VALUES (?,?,?)', (ext, path, fname))

    # Get all data from database
    cursor.execute('SELECT * FROM files')
    rows = cursor.fetchall()

    if os.path.exists(py_path + 'files-part1.txt'):
        os.remove(py_path + 'files-part1.txt')

    # Print query to .txt file
    with open(py_path + 'files-part1.txt', 'a+') as f:
        for row in rows:
            f.write(str(row) + '\n')

    connection.commit()

    connection.close()


if __name__ == '__main__':
    main()
