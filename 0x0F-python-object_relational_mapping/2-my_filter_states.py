#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states
table of the hbtn_0e_0_usa where name matches the argument
"""
from sys import argv

if __name__ == "__main__":
    import MySQLdb
    try:
        db = MySQLdb.connect(host='localhost', user=argv[1],
                             passwd=argv[2], db=argv[3],
                             port=3306, charset="utf8")
        cur = db.cursor()
        query = "SELECT * FROM states WHERE name='%s' ORDER BY id"
        cur.execute(query % (argv[4],))
        rows = cur.fetchall()
        cur.close()
        db.close()
        for row in rows:
            print(row)
    except MySQLdb.Error:
        print("An Error occured, Try again later")
