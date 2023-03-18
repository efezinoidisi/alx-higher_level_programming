#!/usr/bin/python3
"""
This module contains the class State
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()


class State(Base):
    """
    State class that links to the mySQL table states
    Args:
    __tablename__ (str): name of the table
    id (int): primary key
    name (string): maximum of 128 characters
    """
    __tablename__ = 'states'

    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        unique=True,
        autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.id}: {self.name}"
