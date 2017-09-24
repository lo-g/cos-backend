# -*- coding: utf-8 -*-
from datetime import datetime

from sqlalchemy import Column
from sqlalchemy.types import Unicode, Integer, DateTime

from cosbackend.model import DeclarativeBase


class Player(DeclarativeBase):
    """
    Player definition.
    """

    __tablename__ = 'player'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(Unicode(255), unique=True, nullable=False)
    defeats = Column(Integer(), default=0)
    created_at = Column(DateTime(), default=datetime.now)

    def __json__(self):
        return {
            'id': self.id,
            'name': self.name,
            'defeats': self.defeats
        }

__all__ = ['Player']
