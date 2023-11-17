#!/usr/bin/python3
"""script that takes in the name of a state as an argument
and lists all cities of that state,
using the database hbtn_0e_4_usa"""
import sys
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT cities.name from cities, states\
                WHERE states.id = cities.state_id and states.name = %s\
                ORDER BY cities.id ASC", (sys.argv[4],))
    result = []
    for row in cur:
        result.append(row[0])
    print(", ".join(result))
