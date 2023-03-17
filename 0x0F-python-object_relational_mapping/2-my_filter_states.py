#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states
table of the hbtn_0e_0_usa where name matches the argument
"""
from sys import argv
import MySQLdb


def connect_db(*args):
    """
    connects to the my sql server and queries the database
    """
    try:
        db = MySQLdb.connect(
            host='localhost',
            user=args[0],
            passwd=args[1],
            db=args[2],
            port=3306,
            charset="utf8")
        cur = db.cursor()
        query = """SELECT * FROM states WHERE name='{}'
        ORDER BY id""".format(args[3])
        cur.execute(query)
        rows = cur.fetchall()
        cur.close()
        db.close()
        for row in rows:
            print(row)
    except MySQLdb.Error:
        print("An Error occured, Try again later")


if __name__ == "__main__":
    _, user, password, db, state = argv
    connect_db(user, password, db, state)
