#!/usr/bin/python3
"""a script that lists all City objects from the database `hbtn_0e_14_usa`
"""

from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys
from model_city import City


if __name__ == "__main__":

    """starting the database"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    """query into the database"""
    obj = session.query(State.name, City.id, City.name).\
        join(City, (State.id == City.state_id)).order_by(City.id).all()
    for objs in obj:
        print("{}: ({}) {}".format(objs[0], objs[1], objs[2]))

    session.close()
