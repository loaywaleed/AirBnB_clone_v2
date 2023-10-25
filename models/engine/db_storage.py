#!/usr/bin/python3
"""Database storage engine"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    """Engine responsible for database storage using sqlalchemy"""
    __engine = None
    __session = None

    def __init__(self):
        """Mysql database instantiation"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNBT_ENV')
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(
                                          HBNB_MYSQL_USER,
                                          HBNB_MYSQL_PWD,
                                          HBNB_MYSQL_HOST,
                                          HBNB_MYSQL_DB), pool_pre_ping=True)
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None, id=None):
        """
        Query all classes or specific one by ID
        """
        allClasses = [User, Place, State, City, Amenity, Review]
        result = {}

        if cls is not None:
            if id is not None:
                obj = self.__session.query(cls).get(id)
                if obj is not None:
                    ClassName = obj.__class__.__name__
                    keyName = ClassName + "." + str(obj.id)
                    result[keyName] = obj
            else:
                for obj in self.__session.query(cls).all():
                    ClassName = obj.__class__.__name__
                    keyName = ClassName + "." + str(obj.id)
                    result[keyName] = obj
        else:
            for clss in allClasses:
                if id is not None:
                    obj = self.__session.query(clss).get(id)
                    if obj is not None:
                        ClassName = obj.__class__.__name__
                        keyName = ClassName + "." + str(obj.id)
                        result[keyName] = obj
                else:
                    for obj in self.__session.query(clss).all():
                        ClassName = obj.__class__.__name__
                        keyName = ClassName + "." + str(obj.id)
                        result[keyName] = obj
        return result

    def new(self, obj):
        """add the object to current database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commits sessions changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an object from current session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Method that reloads database"""
        Base.metadata.create_all(self.__engine)
        session_opts = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_opts)
        self.__session = Session()

    def close(self):
        """method for closing session"""
        self.__session.close()
