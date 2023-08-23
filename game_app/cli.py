import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, Game, Platform, game_platform_association

DATABASE_URL = "sqlite:///./games.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

