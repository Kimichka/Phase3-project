from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from game_app.models import Base, Game, Platform, game_platform_association

DATABASE_URL = "sqlite:///./games.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def main():
    while True:
        print("\n--- Game Collection Management ---")
        print("1. Add game")
        print("2. List all games")
        print("3. Filter games by platform")
        print("4. Edit a game")
        print("5. Delete a game")
        print("6. Search by game title")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add()
        elif choice == "2":
            list_games()
        elif choice == "3":
            filter_by_platform()
        elif choice == "4":
            edit()
        elif choice == "5":
            delete()
        elif choice == "6":
            search()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Hmm... I didn't get that buddy. Try again?")

def add():
    title = input("Title of the game: ")
    platforms = input("Platforms for the game (separated by commas like PS2,PC): ")

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

    print(f"Added game {title} for platforms: {platforms}")
    session.close()

def list_games():
    session = Session()
    games = session.query(Game).all()

    for game in games:
        platforms = ", ".join([platform.name for platform in game.platforms])
        print(f"{game.title} - Platforms: {platforms}")

    session.close()

def filter_by_platform():
    platform = input("Platform to filter games like PS2, PC: ")

    session = Session()
    platform_obj = session.query(Platform).filter_by(name=platform.strip()).first()
    
    if not platform_obj:
        print(f"No games found for this platform: {platform}")
        session.close()
        return

    games_for_platform = platform_obj.games
    for game in games_for_platform:
        print(game.title)

    session.close()

def edit():
    game_id = int(input("ID of the game you want to edit: "))
    new_title = input("New title of the game: ")

    session = Session()
    game = session.query(Game).filter_by(id=game_id).first()

    if not game:
        print(f"No game found with ID: {game_id}")
        session.close()
        return

    game.title = new_title
    session.commit()

    print(f"Game with ID {game_id} updated to title: {new_title}")
    session.close()

def delete():
    game_id = int(input("ID of the game you want to delete: "))

    session = Session()
    game = session.query(Game).filter_by(id=game_id).first()

    if not game:
        print(f"No game found with ID: {game_id}")
        session.close()
        return

    session.delete(game)
    session.commit()

    print(f"Game with ID {game_id} deleted.")
    session.close()

def search():
    title_query = input("Enter the game title or part of it to search: ")

    session = Session()
    games = session.query(Game).filter(Game.title.like(f"%{title_query}%")).all()

    if not games:
        print(f"No games found with title containing: {title_query}")
        session.close()
        return

    for game in games:
        platforms = ", ".join([platform.name for platform in game.platforms])
        print(f"{game.title} - Platforms: {platforms}")

    session.close()

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    main()
