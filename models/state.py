#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)


    cities = relationship('City', backref='state',
                          cascade='all, delete, delete-orphan')


    @property
    def cities(self):
        """Getter attribute that returns the list of City instances
        with state_id equals to the current State.id"""
        from models import storage
        cities_list = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                cities_list.append(city)
        return cities_list
