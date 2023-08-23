import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, Game, Platform, game_platform_association

DATABASE_URL = "sqlite:///./games.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

@click.group()
@click.command()
@click.option('--title', prompt=True, help="Title of the game.")
@click.option('--platforms', prompt=True, help="Platforms for the game, separated by commas (e.g., PS2,PC).")
def add(title, platforms):
    session = Session()

    platform_list = platforms.split(',')
    platform_objects = []

    for platform_name in platform_list:
        platform_obj = session.query(Platform).filter_by(name=platform_name.strip()).first()
        if not platform_obj:
            platform_obj = Platform(name=platform_name.strip())
            session.add(platform_obj)
        platform_objects.append(platform_obj)
    
    new_game = Game(title=title)
    new_game.platforms = platform_objects
    session.add(new_game)
    session.commit()

    click.echo(f"Added game {title} for platforms: {platforms}")
    session.close()

def cli():
    pass

cli.add_command(add)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    cli()
