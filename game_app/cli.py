from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from game_app.models import Base, Game, Platform

DATABASE_URL = "sqlite:///./games.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def main_menu():
    return input("""
--- Game Collection Management ---
1. Add game
2. List all games
3. Filter games by platform
4. Edit a game
5. Delete a game
6. Search by game title
7. Exit
Enter your choice: """)

def add_game(session):
    title = input("Title of the game: ")
    platforms = [session.query(Platform).get_or_404(name.strip()) or Platform(name=name.strip()) for name in input("Platforms (e.g. PS2,PC): ").split(',')]
    session.add(Game(title=title, platforms=platforms))
    session.commit()

def list_games(session):
    for game in session.query(Game).all():
        print(f"{game.title} - Platforms: {', '.join(platform.name for platform in game.platforms)}")

def filter_by_platform(session):
    platform_name = input("Platform (e.g. PS2, PC): ").strip()
    platform = session.query(Platform).filter_by(name=platform_name).first()
    if platform:
        for game in platform.games:
            print(game.title)
    else:
        print(f"No games found for platform: {platform_name}")

def edit_game(session):
    game_id = int(input("Game ID to edit: "))
    game = session.query(Game).get(game_id)
    if game:
        game.title = input("New game title: ")
        session.commit()
    else:
        print(f"No game found with ID {game_id}")

def delete_game(session):
    game_id = int(input("Game ID to delete: "))
    game = session.query(Game).get(game_id)
    if game:
        session.delete(game)
        session.commit()
    else:
        print(f"No game found with ID {game_id}")

def search_game(session):
    title_query = input("Game title to search: ")
    games = session.query(Game).filter(Game.title.like(f"%{title_query}%")).all()
    for game in games:
        print(f"{game.title} - Platforms: {', '.join(platform.name for platform in game.platforms)}")

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    with Session() as session:
        while (choice := main_menu()) != "7":
            {
                "1": add_game,
                "2": list_games,
                "3": filter_by_platform,
                "4": edit_game,
                "5": delete_game,
                "6": search_game
            }.get(choice, lambda s: print("Invalid choice!"))(session)
