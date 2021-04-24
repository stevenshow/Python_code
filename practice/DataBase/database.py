import sqlite3
import os
import pprint

# cursor.execute('''CREATE TABLE calorie_count (
#                 day TEXT,
#                 calories INTEGER,
#                 weight REAL)''')

def main():
    path = os.path.dirname(__file__) + '/'
    db_path = path + 'dbFile.sqlite3'
    connection = sqlite3.connect(db_path)
    print('Connection to database is complete')
    cursor = connection.cursor()

    user = ''
    while user.lower() != 'q':
        user = input('Would you like to (e)nter data or (r)ead data from the database, or (q)uit?: ')
        if user.lower() == 'e':
            user = input("Place your data in a tuple like such 04/23/21, 1493, 142.3: ")
            data = user.split(',')
            cursor.execute('''INSERT INTO calorie_count VALUES (?,?,?)''', (data[0], data[1], data[2]))
            connection.commit()
        elif user.lower() == 'r':
            cursor.execute('SELECT * FROM calorie_count')
            data = cursor.fetchall()
            pprint.pprint(data)
        else: continue



if __name__ == '__main__':
    main()