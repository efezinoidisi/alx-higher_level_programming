#!/usr/bin/python3
"""
This script lists all City objects from the database hbtn_0e_101_usa
"""
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, exc
from relationship_city import City
from relationship_state import State


def list_state_city():
    """
    Connect to the database and query database
    """
    _, username, password, db = argv
    try:
        engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost/{db}',
            pool_pre_ping=True)
        Session = sessionmaker(engine)
        session = Session()
        cities = session.query(City)
        for city in cities:
            print(f'{city.id}: {city.name} -> {city.state.name}')

    except exc.SQLAlchemyError as err:
        print("something went wrong")

    finally:
        session.close()
        engine.dispose()


if __name__ == "__main__":
    list_state_city()
