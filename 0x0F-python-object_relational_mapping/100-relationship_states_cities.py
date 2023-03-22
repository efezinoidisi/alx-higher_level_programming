#!/usr/bin/python3
"""
start link class to table in database
This script creates the State 'Louisiana' with the City 'San Francisco'
from the database hbtn_0e_100_usa
"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker


def main():
    """
    connect to the database and query database

    Args:
          username (str): mysql username
          password (str): mysql password
          db (str): database name
    """
    _, username, password, db = argv

    try:
        engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost/{db}',
            pool_pre_ping=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(engine)
        session = Session()
        state = State(name="California")
        city = City(name="San Francisco")
        state.cities.append(city)
        session.add(state)
        session.add(city)
        session.commit()

    except exc.SQLAlchemyError as err:
        print(err)
    finally:
        session.close()
        engine.dispose()


if __name__ == "__main__":
    main()
