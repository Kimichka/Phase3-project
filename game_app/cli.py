import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from game_app.models import Base, Game, Platform, game_platform_association

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
        click.echo(f"{game.id}. {game.title} - Platforms: {platforms}")

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
        click.echo(f"{game.id}. {game.title}")

    session.close()

@click.command()
@click.option('--id', prompt=True, type=int, help="ID of the game you want to edit.")
@click.option('--new-title', prompt=True, help="New title of the game.")
def edit(id, new_title):
    """Edit a game's details."""
    session = Session()
    game = session.query(Game).filter_by(id=id).first()

    if not game:
        click.echo(f"No game found with ID: {id}")
        session.close()
        return

    game.title = new_title
    session.commit()

    click.echo(f"Game with ID {id} updated to title: {new_title}")
    session.close()

@click.command()
@click.option('--id', prompt=True, type=int, help="ID of the game you want to delete.")
def delete(id):
    """Delete a game from the collection."""
    session = Session()
    game = session.query(Game).filter_by(id=id).first()

    if not game:
        click.echo(f"No game found with ID: {id}")
        session.close()
        return

    session.delete(game)
    session.commit()

    click.echo(f"Game with ID {id} deleted.")
    session.close()

@click.command()
@click.option('--title', prompt=True, help="Title (or part of the title) of the game you want to search for.")
def search(title):
    """Search for a game by its title."""
    session = Session()
    matching_games = session.query(Game).filter(Game.title.ilike(f"%{title}%")).all()

    if not matching_games:
        click.echo(f"No games found with title containing: {title}")
        session.close()
        return

    for game in matching_games:
        platforms = ", ".join([platform.name for platform in game.platforms])
        click.echo(f"{game.id}. {game.title} - Platforms: {platforms}")

    session.close()

cli.add_command(add)
cli.add_command(list_games)
cli.add_command(filter_by_platform)
cli.add_command(edit)
cli.add_command(delete)
cli.add_command(search)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    cli()
