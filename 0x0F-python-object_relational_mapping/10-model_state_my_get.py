#!/usr/bin/python3
"""
a script that prints the State object with the name
passed as argument from the database `hbtn_0e_6_usa`
"""

from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":

    """connecting to the database"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    state = sys.argv[4]
    Session = sessionmaker(bind=engine)
    session = Session()

    """query the database for state_id"""
    state_name = session.query(State).filter_by(name=state).first()
    if state_name:
        print("{:d}".format(state_name.id))
    else:
        print("Not found")

    session.close()
