#!/usr/bin/python3
"""
Program: ALX  Africa
Dev: Ikary Ryann
Desc:  lists all State objects from
the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    # - generate database schema
    Base.metadata.create_all(engine)

    # - create a new session
    Session = sessionmaker(bind=engine)
    session = Session()

    # - fetch all value in database
    state = session.query(State).order_by(State.id)

    # - print value
    for n in state:
        print('{}: {}'.format(n.id, n.name))

    # - close session
    session.close()
