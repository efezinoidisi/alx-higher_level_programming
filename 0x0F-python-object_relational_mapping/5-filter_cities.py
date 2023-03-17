#!/usr/bin/python3
"""
This module contains a script that takes in the name of a
state as an argument and lists all cities
of that state from the database hbtn_0e_0_usa
"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    try:
        db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2],
                             db=argv[3], port=3306, charset="utf8")
        cur = db.cursor()
        query = """SELECT c.name FROM cities AS c
        INNER JOIN states AS s ON c.state_id = s.id
        WHERE s.name = %s ORDER BY c.id"""
        cur.execute(query, (argv[4],))
        rows = cur.fetchall()
        cur.close()
        db.close()
        my_list = [x for row in rows for x in row]
        print(", ".join(my_list))
    except MySQLdb.Error:
        print("An Error occured, Try again later")
