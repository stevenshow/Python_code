# import required modules
import mariadb
import sys

try:
    conn = mariadb.connect(
        user="root",
        password="sucker01",
        host="localhost",
        port=3306,
        database="CookBook"
    )
    print("Successfully connected CookBook Database!")
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit()

cur = conn.cursor()
