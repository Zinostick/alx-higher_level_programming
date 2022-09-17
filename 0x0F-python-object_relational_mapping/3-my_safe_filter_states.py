#!/usr/bin/python3
"""
Takes argument and displays all values in the state table
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    curs = db.cursor()
    curs.execute("SELECT * \
    FROM states \
    WHERE CONVERT(`name` USING Latin1) \
    COLLATE Latin1_General_CS = %s;", (sys.argv[4],))
    states = curs.fetchall()

    for state in states:
        print(state)
