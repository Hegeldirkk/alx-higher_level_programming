#!/usr/bin/python3
"""
Program: ALX  Africa
Dev: Ikary Ryann
Desc:  lists all State objects from
the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    db = engine.connect()
    trans = db.begin()
    fetch = db.execute('SELECT * FROM {}'.format(State.__tablename__))
    res = fetch.fetchall()
    for n in range(len(res)):
        print('{}: {}'.format(res[n][0], res[n][1]))
    db.close()
