#!/usr/bin/python3
""" City Module Creation """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
import models


class City(BaseModel, Base):
    """ City class that models a city """
    if models.type_storage == "db":
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    else:
        name = ""
        state_id = ""
