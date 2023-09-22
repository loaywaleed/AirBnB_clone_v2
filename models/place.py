#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from models import type_storage
from sqlalchemy.orm import relationship
from models.review import Review

place_amenity = Table('place_amenity', Base.metadata,
                      Column("place_id", String(60), ForeignKey(
                          'places.id'), primary_key=True, nullable=False),
                      Column("amenity_id", String(60), ForeignKey(
                          'amenities.id'), primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    if type_storage == 'db':
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship('Review', backref='place',
                               cascade="all, delete, delete-orphan")
        amenities = relationship(
            "Amenity", secondary=place_amenity, viewonly=False,
            backref='place_amenities')

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    @property
    def reviews(self):
        """Getter for reviews"""
        from models import storage
        lst = []
        all_reviews = storage.all(Review)
        for review in all_reviews.values():
            if self.id == review.place_id:
                lst.append(review)
        return lst

    @property
    def amenities(self):
        """Getter attribute for amenities"""
        from models import storage
        from models.amenity import Amenity
        lst_of_amenities = []
        all_amenities = storage.all(Amenity)
        for amenity in all_amenities.values():
            if self.id == amenity.id:
                lst_of_amenities.append(amenity)
        return lst_of_amenities

    @amenities.setter
    def amenities(self, obj):
        """Setter attribute for amenities"""
        from models.amenity import Amenity
        if obj is not None:
            if isinstance(obj, Amenity):
                if obj.id not in self.amenity_ids:
                    self.amenity_ids.append(obj.id)
