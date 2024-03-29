#!/usr/bin/python3
""" lists all states with a name starting with N """


import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            database=sys.argv[3]
            )
    name_searched = sys.argv[4]
    cur = conn.cursor()
    cur.execute("SELECT * \
                FROM states \
                WHERE BINARY name = '{}' \
                ORDER BY states.id ASC".format(name_searched))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
