#!/usr/bin/python3
"""Safe from sql injection"""
import sys
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                (sys.argv[4],))
    for row in cur:
        print(row)
