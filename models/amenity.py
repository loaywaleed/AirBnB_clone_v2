#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import type_storage
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    if type_storage == 'db':
        from models.place import place_amenity
        name = Column(String(128), nullable=False)
        place_amenities = relationship('Place', secondary=place_amenity)

    else:
        name = ""
