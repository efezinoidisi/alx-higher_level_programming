#!/usr/bin/python3
"""
This module contains a script that lists all cities
from the database hbtn_0e_4_usa
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
        query = """SELECT c.id, c.name, s.name FROM cities AS c
        INNER JOIN states AS s ON c.state_id = s.id
        ORDER BY c.id"""
        cur.execute(query)
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as err:
        print(err)
    finally:
        cur.close()
        db.close()


if __name__ == "__main__":
    _, username, password, dbname = argv
    connect_to_db(username, password, dbname)
