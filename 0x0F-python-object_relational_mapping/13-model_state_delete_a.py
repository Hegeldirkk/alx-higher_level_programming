#!/usr/bin/python3
"""
Program: ALX Africa
Dev: Ikary Ryann
Desc: deletes all State objects with a name
containing the letter a from the database
hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # - connect to daatabase
    engine = create_engine('mysql://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    # - generated database schema
    Base.metadata.create_all(engine)

    # - create session
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    session = Session()

    # - delete all elements containing a
    session.query(State).filter(State.name.ilike('%a%')
                                ).delete(synchronize_session='fetch')
    session.commit()

    # - close session
    session.close()
