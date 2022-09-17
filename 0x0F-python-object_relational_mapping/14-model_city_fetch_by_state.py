#!/usr/bin/python3
"""
Program: ALX  Africa
Dev: Ikary Ryann
Desc:prints all City objects
from the database hbtn_0e_14_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # - connect to database
    engine = create_engine('mysql://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    # - generated database schema
    Base.metadata.create_all(engine)

    # - create session
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    session = Session()

    # - fetch all city in database
    cities = session.query(City, State)\
        .filter(City.state_id == State.id).order_by(City.id.asc())\
        .all()
    # - prints all data
    for resCity, resState in cities:
        print('{}: ({}) {}'.format(resState.name, resCity.id, resCity.name))
