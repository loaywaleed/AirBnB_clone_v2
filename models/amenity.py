#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import type_storage
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import place_amenity


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    if type_storage == 'db':
        name = Column(String(128), nullable=False)

    else:
        name = ""
