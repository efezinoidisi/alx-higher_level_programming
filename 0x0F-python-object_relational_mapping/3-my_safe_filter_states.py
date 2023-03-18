#!/usr/bin/python3
"""
This script is the version of module '2-my_filter_states.py'
that is safe from a sql injection attack
"""
from sys import argv
import MySQLdb


def connect_to_db(username, password, dbname, state):
    """
    connects to the my sql server and queries the database
    """
    try:
        db = MySQLdb.connect(host='localhost', user=username,
                             passwd=password, db=dbname,
                             port=3306, charset="utf8")
        cur = db.cursor()
        query = "SELECT * FROM states WHERE name=%s ORDER BY id"
        cur.execute(query, (state,))
        rows = cur.fetchall()
        cur.close()
        db.close()
        for row in rows:
            print(row)
    except MySQLdb.Error:
        print("An Error occured, Try again later")


if __name__ == "__main__":
    _, username, password, dbname, state = argv
    connect_to_db(username, password, dbname, state)
