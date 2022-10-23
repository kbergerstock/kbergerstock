"""
python BREAK_OUT 
select_view.py
krbergerstck june ,2020
"""

import random
import const
import arcade

from arcade     import color
from game_data  import Game

class serveView(arcade.View):
    def __init__(self, game, SelectView):
        super().__init__()
        self.game = game
        self.selectView = SelectView
        self.key_code = 0
        self.msg = 0
        self.dir = 0
        

    def on_show(self):
        self.msg = 1
        self.dir = 0
        arcade.set_background_color(const.SCREEN_COLOR)
        self.game.balls.home()
               

    def on_draw(self):
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.            
        arcade.start_render()
        self.game.render()
        self.game.render_score(const.SCREEN_WIDTH-150,const.SCREEN_HEIGHT-35,color.ALICE_BLUE,24,const.GAME_FONT[0])
        if self.msg == 1:
            arcade.draw_text('LEVEL {0}'.format(Game.level),0,300,color.ALICE_BLUE,
                    font_size=48,width=const.SCREEN_WIDTH,align='center',font_name=const.GAME_FONT[0])
            arcade.draw_text('LIVES REMAINING {0}'.format(Game.health),0,200,color.ALICE_BLUE,
                    font_size=32,width=const.SCREEN_WIDTH,align='center',font_name=const.GAME_FONT[0])
            arcade.draw_text('TO SERVE PRESS <SPACE> OR <B>',0,100,color.ALICE_BLUE,
                    font_size=32,width=const.SCREEN_WIDTH,align='center',font_name=const.GAME_FONT[0])
        elif self.msg == 2:
            self.game.paddle.home()
            self.selectView('level_view')
            self.msg = 1    
    
    
    def update(self,delta_time):
        self.game.update(delta_time)
        self.game.paddle.update(delta_time, self.dir)


    def on_key_press(self, symbol: int, modifiers: int):
        self.key_code = symbol
        if symbol == 32 or symbol == 98:
            self.msg += 1
        if symbol == 65361:
            self.dir = -1
        elif symbol == 65363:
            self.dir = 1


    def on_key_release(self, _symbol: int, _modifiers: int):
        if _symbol == 65361 or _symbol == 65363:
            self.dir = 0
