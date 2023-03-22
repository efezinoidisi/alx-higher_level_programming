#!/usr/bin/python3
"""
This script lists all State objects and corresponding City objects
contained in the database hbtn_0e_101_usa
"""
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, exc
from relationship_state import State
from relationship_city import City


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
        states = session.query(State)
        for state in states:
            print(f'{state.id}: {state.name}')
            for city in state.cities:
                print(f'\t{city.id}: {city.name}')

    except exc.SQLAlchemyError as err:
        print("something went wrong")

    finally:
        session.close()
        engine.dispose()


if __name__ == "__main__":
    list_state_city()
