# Batter

What's your batting average? Find out with this terminal version of the arcade classic. The goal is simple. Just bat the ball at the blricks until there are none left. If you miss the ball the game is over.

## Getting Started
--
Make sure you have Python 3.8.0 or newer and asciimatics 1.12.0 or new installed and running on your machine. You can install Asciimatics by opening a terminal and running the following command.
```
python3 -m pip install asciimatics
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.
```
python3 batter 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- batter              (source code for game)
  +-- game              (specific game classes)
    +-- __init__.py                 (phyton package file)
    +-- action.py                   (action class)
    +-- actor.py                    (actor class)
    +-- constant.py                 (constant file)
    +-- control_actors_action.py    (ControlActorsAction class)
    +-- director.py                 (director class)
    +-- draw_actors_action.py       (DrawActorsAction class)
    +-- handle_collisions_action.py (HandleCollisionsAction class)
    +-- input_service.py            (InputService class)
    +-- move_actors_action.py       (MoveActorsAction class)
    +-- output_services.py          (OutputService class)
    +-- point.py                    (Point class)
    +-- play.py                     (Play class)
  +-- __init__.py       (python package file)
  +-- __main__.py      (entry point for program)
+-- README.md           (general info)
```
## Required Technologies
--
* Python 3.8.0
* Asciimatics 1.12.0

## Authors
--

* Nicolas Paredes: par21035@byui.edu
* Helama Barbour: Helamashi@gmail.com
* James Charlie Salva: jamessalvajames@hotmail.com
