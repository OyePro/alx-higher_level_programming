#!/usr/bin/python3
"""
a script that changes the name of a State object
from the database `hbtn_0e_6_usa`
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

    """query into the database and updating the value of state"""
    session.query(State).filter(State.id == 2).update(
            {State.name: 'New Mexico'}, synchronize_session=False)
    session.commit()

    session.close()
