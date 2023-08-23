import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, Game, Platform, game_platform_association
