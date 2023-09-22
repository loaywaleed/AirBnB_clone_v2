#!/usr/bin/python3
""" City Module Creation """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Constraint
import models


class City(BaseModel, Base):
    """ City class that models a city """
    __tablename__ = "cities"
    if models.type_storage == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    else:
        name = ""
        state_id = ""
