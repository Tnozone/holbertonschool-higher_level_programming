#!/usr/bin/python3
<<<<<<< HEAD


""" Lists all states from the database sorted in ascending order """


import MySQLdb
import sys


if __name__ == "__main__":
    """ main fucntion """

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2],
            db=argv[3])
    st = db.cursor()
    st.execute("""SELECT `id`, `name` FROM states ORDER BY `id`;""")
    res = st.fetchall()
    for i in res:
        print(i)
    db.close()
>>>>>>> 143f3f0714e0d3ad05316566215efe56a7832bcf
