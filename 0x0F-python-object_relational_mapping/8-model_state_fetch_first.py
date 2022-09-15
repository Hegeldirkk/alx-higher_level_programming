#!/usr/bin/python3
"""
Program: ALX Africa
Dev: Ikary Ryann
Desc: prints the first State object
from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    # - generate database schema
    Base.metadata.create_all(engine)

    # - create session orm
    Session = sessionmaker(bind=engine)
    session = Session()

    # - fetch the first value in database
    state = session.query(State).first()

    # - print value fetch
    if state is None:
        print('Nothing')
    else:
        print('{}: {}'.format(state.id, state.name))
    session.close()
