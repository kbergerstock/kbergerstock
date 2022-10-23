"""
python BREAK_OUT 
level_view.py
krbergerstck june ,2020
"""

import random
import const
import arcade
from arcade     import color
from game_data  import Game

class levelView(arcade.View):
    def __init__(self, game, SelectView):
        super().__init__()
        self.game = game
        self.selectView = SelectView
        self.dir = 0

    def on_show(self):
        self.dir = 0
        arcade.set_background_color(const.SCREEN_COLOR)
    
    def on_draw(self):
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.            
        arcade.start_render()
        self.game.render()
        arcade.set_viewport(0,const.SCREEN_WIDTH,5,const.SCREEN_HEIGHT - 5)
             
    
    def update(self, delta_time):
        self.game.update(delta_time)
        self.game.paddle.update(delta_time, self.dir)
        if self.game.balls.update(self.game.paddle, self.game.bricks):
            self.selectView('serve_view')


    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == 65361:
            self.dir = -1
        elif symbol == 65363:
            self.dir = 1


    def on_key_release(self, _symbol: int, _modifiers: int):
        if _symbol == 65361 or _symbol == 65363:
            self.dir = 0


