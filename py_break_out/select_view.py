"""
python BREAK_OUT 
select_view.py
krbergerstck june ,2020
"""

import const
import arcade
import random


from arcade     import color
from game_data  import Game

class selectView(arcade.View):
    def __init__(self, game, SelectView):
        super().__init__()
        self.game = game
        self.selectView = SelectView
        self.key_code = 0
        self.msg = 0

    def on_show(self):
        self.msg = 1
        arcade.set_background_color(const.SCREEN_COLOR)

    def on_draw(self):
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.            
        arcade.start_render()
        self.game.render()
        self.game.render_score(const.SCREEN_WIDTH-150,const.SCREEN_HEIGHT-35,color.ALICE_BLUE,24,const.GAME_FONT[0])
        if self.msg == 1:
            arcade.draw_text('PRESS UP/DN TO CHANGE PADDLE_COLOR',0,150,color.ALICE_BLUE,
                    font_size=24,width=const.SCREEN_WIDTH,align='center',font_name=const.GAME_FONT[1])
            arcade.draw_text('PRESS <SPACE> OR <B> TO SELECT',0,100,color.ALICE_BLUE,
                    width=const.SCREEN_WIDTH,align='center',font_size=24,font_name=const.GAME_FONT[1])
        elif self.msg == 2:
            self.selectView('serve_view')
        else:
            self.msg = 1   


    def update(self,delta_time):
        self.game.update(delta_time)


    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == 32 or symbol == 98:
            self.msg += 1
        elif symbol == 65362 and self.msg == 1:
            self.game.paddle.inc_texture()
        elif symbol == 65364 and self.msg == 1:       
            self.game.paddle.dec_texture()

        self.key_code = symbol