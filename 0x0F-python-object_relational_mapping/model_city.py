#!/usr/bin/python3
"""Program: ALX  Africa
Dev: Ikary Ryann
Desc:contains the class definition of a
State and an instance Base = declarative_base()
model city
"""

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """class definition of a City"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
