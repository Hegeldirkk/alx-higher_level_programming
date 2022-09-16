#!/usr/bin/python3
"""
Program:ALX Africa
Dev: Ikary Ryann
Desc: lists all State objects that contain
the letter a from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # - connect to database
    engine = create_engine('mysql://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    # - generate database schema
    Base.metadata.create_all(engine)

    # - create session
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    session = Session()

    # - fetch all data in db using a letter 'a'
    state = session.query(State).filter(State.name.ilike("%a%")).all()

    # - print data
    for n in state:
        print('{}: {}'.format(n.id, n.name))
    session.close()
