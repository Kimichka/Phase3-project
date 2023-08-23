# Game Collection CLI Project

## Welcome everyone

This tool helps you manage your video game collection and the platforms they are available on, using SQL.

## Setup

The project uses a virtual environment, in order to install it follow these steps:

$ pipenv install sqlalchemy alembic

## Usage

Navigate to the directory and run the project

$ python run.py

1. Adding a Game:

Select 1 from the main menu.
Enter the game's title.
Enter the platforms it's available on separated by commas (e.g., "PS4, PC").

2. Listing All Games:

Select 2 from the main menu.
All games and their associated platforms will be displayed.

3. Filtering Games by Platform:

Select 3 from the main menu.
Enter the platform name to filter games.

4. Editing a Game:

Select 4 from the main menu.
Provide the game ID and the new title.

5. Deleting a Game:

Select 5 from the main menu.
Enter the game ID to delete.

6. Searching for a Game by Title:

Select 6 from the main menu.
Enter the title of the game to search.

7. Exiting:

Select 7 from the main menu to exit the tool.

