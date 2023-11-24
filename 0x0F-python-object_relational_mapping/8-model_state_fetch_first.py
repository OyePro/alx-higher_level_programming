#!/usr/bin/python3
"""a script that prints the first State object from the
database `hbtn_0e_6_usa`
"""

from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":

    # starting the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # query the first object in database
    first_obj = session.query(State).order_by(State.id).first()
    if first_obj:
        print("{:d}: {:s}".format(first_obj.id, first_obj.name))
    else:
        print("Nothing")

    session.close()
