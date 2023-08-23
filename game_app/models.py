from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

game_platform_association = Table('game_platform', Base.metadata,
    Column('game_id', Integer, ForeignKey('games.id')),
    Column('platform_id', Integer, ForeignKey('platforms.id')))

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True, nullable=False)
    platforms = relationship('Platform', secondary=game_platform_association, back_populates='games')

class Platform(Base):
    __tablename__ = 'platforms'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    games = relationship('Game', secondary=game_platform_association, back_populates='platforms')