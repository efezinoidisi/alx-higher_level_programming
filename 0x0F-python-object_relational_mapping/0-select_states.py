#!/usr/bin/python3
"""
This module contains a script that lists all states
from the database hbtn_0e_0_usa
"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    try:
        db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2],
                             db=argv[3], port=3306, charset="utf8")
        cur = db.cursor()
        cur.execute("SELECT * FROM states ORDER BY id")
        rows = cur.fetchall()
        cur.close()
        db.close()
        for row in rows:
            print(row)
    except MySQLdb.Error:
        print("An Error occured, Try again later")
