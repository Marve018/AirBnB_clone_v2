#!/usr/bin/python3
"""
module defines a class to manage db storage for hbnb clone
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage():
    """ dbstorage class """
    __engine = None
    __session = None

    def __init__(self):
        """ Initializer """
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, password, host, database), pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
            Current db query
            returns a dictionary
        """
        classes = (State, City, User, Place, Review, Amenity)
        dic = {}

        if cls is None:
            for item in classes:
                query = self.__session.query(item)
                for element in query.all():
                    o_key = "{}.{}".format(element.__class__.__name__,
                                           element.id)
                    dic[o_key] = element

        else:
            query = self.__session.query(cls)
            for element in query.all():
                o_key = "{}.{}".format(element.__class__.__name__, element.id)
                dic[o_key] = element

        return dic

    def new(self, obj):
        """ Add object to current db session """
        self.__session.add()
        self.save()

    def save(self):
        """ commit all changes """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete current db session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ reload all """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()

    def close(self):
        """ query close """
        self.__session.close()
