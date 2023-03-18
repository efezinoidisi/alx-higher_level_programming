#!/usr/bin/python3
"""
start link class to table in database
This script lists all City objects from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine, select, exc, asc
from sqlalchemy.orm import sessionmaker


def query_db(username, password, db):
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
        Base.metadata.create_all(engine)
        Session = sessionmaker(engine)
        session = Session()
        query = session.query(
            State.name, City.id, City.name).join(State).order_by(City.id)
        for res in query:
            print(f"{res[0]}: ({res[1]}) {res[2]}")

    except exc.SQLAlchemyError as err:
        print("something went wrong")
    finally:
        session.close()
        engine.dispose()


if __name__ == "__main__":
    _, username, password, db = argv
    query_db(username, password, db)
