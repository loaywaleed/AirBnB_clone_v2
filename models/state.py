#!/usr/bin/python3
""" State Module """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models.city import City
from models import type_storage
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class that models a state """
    __tablename__ = "states"
    if type_storage == "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')
    else:
        name = ""

    if type_storage != "db":
        @property
        def cities(self):
            """ list of city instances"""
            from models import storage
            list_of_cities = []
            all_cities = storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    list_of_cities.append(city)
            return list_of_cities
