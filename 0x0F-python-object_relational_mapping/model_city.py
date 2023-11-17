#!/usr/bin/python3
"""
file that contains the class definition of a State
and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    State class that inherits from Base
    """
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
