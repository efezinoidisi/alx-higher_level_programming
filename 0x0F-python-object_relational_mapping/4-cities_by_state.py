#!/usr/bin/python3
"""
This module contains a script that lists all cities
from the database hbtn_0e_0_usa
"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    try:
        db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2],
                             db=argv[3], port=3306, charset="utf8")
        cur = db.cursor()
        query = """SELECT c.id, c.name, s.name FROM cities AS c
        INNER JOIN states AS s ON c.state_id = s.id
        ORDER BY c.id"""
        cur.execute(query)
        rows = cur.fetchall()
        cur.close()
        db.close()
        for row in rows:
            print(row)
    except MySQLdb.Error:
        print("An Error occured, Try again later")
