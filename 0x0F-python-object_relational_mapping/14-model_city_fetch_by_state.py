#!/usr/bin/python3
"""
start link class to table in database
This script lists all City objects from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base
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
        # Base.metadata.create_all(engine)
        Session = sessionmaker(engine)
        session = Session()
        query = select(City).order_by(asc(City.id))
        for city in session.scalars(query):
            print(city)
    except exc.SQLAlchemyError as err:
        print(err)
    finally:
        session.close()
        engine.dispose()


if __name__ == "__main__":
    _, username, password, db = argv
    query_db(username, password, db)
