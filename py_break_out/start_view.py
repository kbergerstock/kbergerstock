"""
python BREAK_OUT 
start_view.py
krbergerstck june ,2020
"""


import random
import const
import pyglet
import arcade
from arcade     import color
from game_data  import Game

class startView(arcade.View):
    def __init__(self,game, SelectView):
        super().__init__()
        self.game = game
        self.selectView = SelectView


    def on_show(self):
        arcade.set_background_color(const.SCREEN_COLOR)
        
    
    def on_draw(self):
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.            
        arcade.start_render()
        self.game.backgnd.draw()
        arcade.draw_text(const.SCREEN_TITLE,0,700,color.GREEN,
                         font_size=48,align='center',width=const.SCREEN_WIDTH,font_name=const.GAME_FONT[0]) 
        self.game.render_scores(450,550,color.ALICE_BLUE,const.GAME_FONT[0])
        self.game.render_score(const.SCREEN_WIDTH-150,const.SCREEN_HEIGHT-35,color.ALICE_BLUE,24,const.GAME_FONT[0])
        arcade.draw_text('to start press button  "B"',0,150,color.ALICE_BLUE,
                         font_size=24,width=const.SCREEN_WIDTH,align='center',font_name=const.GAME_FONT[1])
        self.game.render_fps(20, 20, color.ALICE_BLUE, 12, const.GAME_FONT[1])
        arcade.set_viewport(0,const.SCREEN_WIDTH,5,const.SCREEN_HEIGHT - 5) 
    
    
    def update(self,delta_time):
        self.game.update(delta_time) 
                
    #over ride the default function defined by arcade
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == 32 or symbol == 98:
            self.selectView('select_view')
                