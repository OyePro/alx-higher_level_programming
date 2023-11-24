#!/usr/bin/python3
"""Defining class of a State using sqlalchemy"""

from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class State which inherits from Base
    it is links to MYSQL table states
    Sequence('user_id_seq')
    """
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
