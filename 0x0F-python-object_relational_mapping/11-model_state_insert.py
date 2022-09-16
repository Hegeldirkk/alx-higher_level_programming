#!/usr/bin/python3
"""
Program: ALX Africa
Dev: Ikary Ryann
Desc: adds the State object “Louisiana”
to the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # - connect to database
    engine = create_engine('mysql://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    # - generated database schema
    Base.metadata.create_all(engine)

    # -  create session
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    session = Session()

    # - add value in database
    name = State(name='Louisiana')
    session.add(name)
    session.commit()

    # - fetch id of a new value
    state = session.query(State).filter(State.name.ilike('Louisiana')).first()
    print('{}'.format(state.id))

    session.close()
