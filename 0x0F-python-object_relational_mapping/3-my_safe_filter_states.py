#!/usr/bin/python3
"""
This script is the version of module '2-my_filter_states.py'
that is safe from a sql injection attack
"""
from sys import argv

if __name__ == "__main__":
    import MySQLdb
    try:
        db = MySQLdb.connect(host='localhost', user=argv[1],
                             passwd=argv[2], db=argv[3],
                             port=3306, charset="utf8")
        cur = db.cursor()
        query = "SELECT * FROM states WHERE name=%s ORDER BY id"
        cur.execute(query, (argv[4],))
        rows = cur.fetchall()
        cur.close()
        db.close()
        for row in rows:
            print(row)
    except MySQLdb.Error:
        print("An Error occured, Try again later")
