from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

game_platform_association = Table('game_platform', Base.metadata,
    Column('game_id', Integer, ForeignKey('games.id')),
    Column('platform_id', Integer, ForeignKey('platforms.id'))
)
