#!/usr/bin/python3
"""
This script lists all states with a name starting with N
"""
from sys import argv
import MySQLdb


def connect_db(name, password, dbase):
    """
    connect to my sql server and query database
    """
    try:
        db = MySQLdb.connect(host='localhost', user=name,
                             passwd=password, db=dbase,
                             port=3306, charset="utf8")
        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
        rows = cur.fetchall()
        cur.close()
        db.close()
        for row in rows:
            print(row)
    except MySQLdb.Error:
        print("An Error occured, Try again later")


if __name__ == "__main__":
    _, name, password, db = argv
    connect_db(name, password, db)
