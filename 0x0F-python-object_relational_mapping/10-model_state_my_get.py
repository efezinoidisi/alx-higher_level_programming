#!/usr/bin/python3
"""
start link class to table in database
This script prints the State object with the name passed as an
argument from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine, select, exc
from sqlalchemy.orm import sessionmaker


def query_db(username, password, db, state):
    """
    connect to the database and query database

    Args:
          username (str): mysql username
          password (str): mysql password
          db (str): database name
    """
    try:
        engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost/{db}',
            pool_pre_ping=True)
        Session = sessionmaker(engine)
        session = Session()
        query = session.query(State.id).where(State.name == state)
        if query.count() != 0:
            for i in query:
                print(i[0])
        else:
            print("Not Found")
    except exc.SQLAlchemyError as err:
        print(err)
    finally:
        session.close()
        engine.dispose()


if __name__ == "__main__":
    _, username, password, db, state = argv
    query_db(username, password, db, state)
