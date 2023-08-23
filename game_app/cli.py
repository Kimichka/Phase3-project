import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, Game, Platform, game_platform_association

DATABASE_URL = "sqlite:///./games.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

@click.group()
def cli():
    """CLI tool to manage your game collection."""
    pass

@click.command()
@click.option('--title', prompt=True, help="Title of the game.")
@click.option('--platforms', prompt=True, help="Platforms for the game are separated by commas like PS2,PC.")
def add(title, platforms):
    """Add a new game to the collection."""
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

@click.command()
def list_games():
    """List all games and their platforms."""
    session = Session()

    games = session.query(Game).all()

    for game in games:
        platforms = ", ".join([platform.name for platform in game.platforms])
        click.echo(f"{game.title} - Platforms: {platforms}")

    session.close()

@click.command()
@click.option('--platform', prompt=True, help="Platform to filter games by, e.g., PS2, PC.")
def filter_by_platform(platform):
    """List games for a specific platform."""
    session = Session()

    platform_obj = session.query(Platform).filter_by(name=platform.strip()).first()
    
    if not platform_obj:
        click.echo(f"No games found for platform: {platform}")
        session.close()
        return

    games_for_platform = platform_obj.games

    for game in games_for_platform:
        click.echo(game.title)

    session.close()

cli.add_command(add)
cli.add_command(list_games)
cli.add_command(filter_by_platform)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    cli()
