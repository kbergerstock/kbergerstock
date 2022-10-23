"""
BREAK_OUT.py main file
krbergerstck oct ,2022

"""

import arcade
from game_data  import Game
from views      import Views
from Sounds     import Sounds

# from memory_profiler import profile
# @profile
def main():
    """ Main method """
    #load all resources    
    Sounds.load()
    Game.load()
    # activate the starting view ie window 
    views = Views()
    views.load(Game)
    # execute the game engine
    arcade.run()

if __name__ == "__main__":
    main()