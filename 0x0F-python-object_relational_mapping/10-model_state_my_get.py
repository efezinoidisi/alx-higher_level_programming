#!/usr/bin/python3
"""
start link class to table in database
This script prints the State object with the name passed as an
argument from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import literal


def main():
    """
    connect to the database and query database

    Args:
          username (str): mysql username
          password (str): mysql password
          db (str): database name
    """
    _, username, password, db, state = argv
    try:
        engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost/{db}',
            pool_pre_ping=True)
        Session = sessionmaker(engine)
        session = Session()
        query = session.query(State.id).filter(State.name == state).first()
        if query:
            print(query[0])
        else:
            print("Not found")
    except exc.SQLAlchemyError as err:
        print(err)
    finally:
        session.close()
        engine.dispose()


if __name__ == "__main__":
    main()
