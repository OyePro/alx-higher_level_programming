#!/usr/bin/python3
"""a script that creates the State “California” with the
City “San Francisco” from the database `hbtn_0e_100_usa`
"""

from relationship_city import City
from relationship_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
import sys


if __name__ == "__main__":

    """starting the database"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    """Creating state `California` with city `San Francisco` """

    newstate = State(name="California")
    newcity = City(name="San Francisco")
    newstate.cities.append(newcity)

    session.add(newstate)
    session.add(newcity)

    session.commit()
    session.close()
