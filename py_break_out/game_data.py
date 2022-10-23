# breakout game data class
# K. r. bergerstock
# 10/21/2020


import random
import time
import const
import arcade
from arcade      import color
from hiscores    import Hiscores
from background  import Background
from ball        import Balls
from paddle      import PADDLE
from bricks      import level_one
from fps         import FPS



class Game():
    score =  0
    health = 3
    level = 0 
    high_scores = None             # high scores list
    backgnd = None                 # moving background sprite list    
    gc = None                      # game controller
    # sprite lists
    bricks = None
    balls = None
    paddle = None
    Fps = None
    
    
    #initialize main screen
    @classmethod
    def load(cls):    
        random.seed()
        # load the textures
        # cls.textures['arrows'] = arcade.load_textures(const.ARROW_TEXTURES,const.ARROW_LOCATIONS)
        cls.backgnd = Background()
        cls.bricks  = level_one()
        cls.balls   = Balls()
        cls.paddle  = PADDLE()
        cls.high_scores = Hiscores('break_out_hi_scores.csv')
        cls.high_scores.create()
        cls.Fps = FPS()

    
    @classmethod
    def new_board(cls):
        cls.bricks = level_one()
        
        
    @classmethod
    def setup(cls):
        cls.score = 0
        cls.health = 3
        cls.level = 1
        
        
    @classmethod
    def update(cls , dt):
        cls.backgnd.update()
        cls.Fps.update(dt)
    
        
    @classmethod
    def render(cls):
        cls.backgnd.draw()   
        cls.render_fps(20, 20, color.ALICE_BLUE, 12, const.GAME_FONT[1]) 
        cls.render_score(const.SCREEN_WIDTH-150,const.SCREEN_HEIGHT-35,color.ALICE_BLUE,24,const.GAME_FONT[0])
        cls.bricks.draw()
        cls.paddle.draw()
        cls.balls.draw()
        
     
    @classmethod
    def render_fps(cls, x, y, color, size, Font):
        _fps = cls.Fps.fps
        arcade.draw_text('{0:03}'.format(_fps), x, y, color, font_size=size, font_name=Font)


    @classmethod
    def render_score(cls, x, y, color, size, Font):
        arcade.draw_text('{0:08}'.format(cls.score),x,y,color,font_size=size,font_name=Font)


    @classmethod
    def render_health(cls, x, y):
        pass

    
    @classmethod
    def render_scores(cls, x , y, Color, Font):
        ''' display the hi score table '''
        arcade.draw_text('HIGH SCORES',0,y,color.ALABAMA_CRIMSON,font_size=32,width=const.SCREEN_WIDTH,align='center',font_name=const.GAME_FONT[0])
        y -= 40
        for  e in cls.high_scores.get():
            arcade.draw_text("{0:>2}".format(e[0]),x,y,Color,font_size=18,font_name=Font)
            arcade.draw_text("{0:<3}".format(e[1]),x+75,y,Color,font_size=18,font_name=Font)
            arcade.draw_text("{0:>8}".format(e[2]),x+150,y,Color,font_size=18,font_name=Font)
            y -= 25

    # activate the draw,update methods for the current view             

       
    

