#!/usr/bin/python3
"""
This module contains the class City which
creates the table cities
"""
from sys import argv
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from model_state import Base, State
from sqlalchemy.orm import relationship


class City(Base):
    """
    City class that links to the mySQL table cities

    Args:
        __tablename__ (str): name of the table
        id (int): primary key
        name (string): maximum of 128 characters
        state_id (int) : links to state table id
    """
    __tablename__ = 'cities'

    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        unique=True,
        autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
