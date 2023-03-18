#!/usr/bin/python3
"""
This module contains a script that lists all states
from the database hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb


def connect_to_db(username, password, dbname):
    """
    connect to the database and query data
    """
    try:
        db = MySQLdb.connect(
            host='localhost',
            user=username,
            passwd=password,
            db=dbname,
            port=3306,
            charset="utf8")
        cur = db.cursor()
        cur.execute("SELECT * FROM states ORDER BY id")
        rows = cur.fetchall()
        cur.close()
        db.close()
        for row in rows:
            print(row)
    except MySQLdb.Error:
        print("An Error occured, Try again later")


if __name__ == "__main__":
    _, username, password, dbname = argv
    connect_to_db(username, password, dbname)
