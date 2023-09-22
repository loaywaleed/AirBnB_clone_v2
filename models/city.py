#!/usr/bin/python3
""" City Module Creation """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Constraint
import models
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ City class that models a city """
    __tablename__ = "cities"
    if models.type_storage == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship('Place', backref='cities',
                              cascade='all, delete, delete-orphan')
    else:
        name = ""
        state_id = ""
