#!/usr/bin/python3
""" States listing module """


import MySQLdb
from sys


if __name__ == "__main__":
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            database=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE CAST(name AS BINARY) LIKE 'N%' \
            ORDER BY states.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
