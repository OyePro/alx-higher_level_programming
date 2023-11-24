#!/usr/bin/python3
"""
a script that adds the State object “Louisiana”
to the database `hbtn_0e_6_usa`
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

    """adding data to the database"""
    louis = State(name='Louisiana')
    session.add(louis)
    session.commit()

    """query into the database and printing the id of Louisiana"""
    for obj in session.query(State).filter_by(name='Louisiana'):
        print("{:d}".format(obj.id))

    session.close()
