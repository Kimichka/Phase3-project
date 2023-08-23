# Game Collection Project

## Welcome everyone

This tool helps you manage your video game collection and the platforms they are available on.

## Setup

The project uses a virtual environment. In order to install, follow these steps:

### $ pipenv install sqlalchemy alembic

If for any reason the code does not work follow steps below:

### Deactivate virtual environment:
### $deactivate

### Reinstall virtual environment:
### $rm -rf game_env

### Recreate the virtual environment:
### $python3 -m venv game_env

### Activate the new environment:
### $source game_env/bin/activate

### Now install:
### $pip install sqlalchemy

## Usage

Navigate to the directory and run the project

### $ python run.py

## 1. Adding a Game:

Select 1 from the main menu.
Enter the game's title.
Enter the platforms it's available on separated by commas (e.g., "PS4, PC").

## 2. Listing All Games:

Select 2 from the main menu.
All games and their platforms will be displayed.

## 3. Filtering Games by Platform:

Select 3 from the main menu.
Enter the platform name to filter games.

## 4. Editing a Game:

Select 4 from the main menu.
Provide the game ID and the new title.

## 5. Deleting a Game:

Select 5 from the main menu.
Enter the game ID to delete.

## 6. Searching for a Game by Title:

Select 6 from the main menu.
Enter the title of the game to search.

## 7. Exiting:

Select 7 from the main menu to exit the tool.

