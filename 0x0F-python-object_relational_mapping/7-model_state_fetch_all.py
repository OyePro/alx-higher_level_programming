#!/usr/bin/python3
"""a script that lists all State objects from the database `hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":

    """starting the database"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    """query into the database"""
    for obj in session.query(State).order_by(State.id):
        print("{:d}: {:s}".format(obj.id, obj.name))

    session.close()