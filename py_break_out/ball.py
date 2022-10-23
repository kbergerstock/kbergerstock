# ball.py
import arcade
import const
import math
import random as rnd
from Sounds import Sounds
        
class BALL(arcade.Sprite):
    ball_textures = arcade.load_textures(const.BALL_TEXTURES,const.BALL_LOCATIOINS)
    
    def __init__(self):
        super().__init__()
        self.speed = const.BALL_VELOCITY
        self.scale = const.BALL_SCALE
        self.angle = rnd.triangular(20,80)
        self.dx = 0.0
        self.dy = 0.0
        self.xdir = rnd.choice([1, -1])
        self.ydir = 1
        self.update_dx_dy()


    @classmethod
    def get_texture(cls, idx):
        return cls.ball_textures[idx]
    
    
    def set_ball_texture(self, idx):
        self.set_texture(idx)


    def createSprite(self, idx):
        for i in range(7):
            self.append_texture(BALL.get_texture(i))
        self.set_position(600,120)
        self.set_texture( idx )
        self.active = False


    def update_dx_dy(self):
        rad = self.angle * math.pi / 180.0
        self.dx = self.xdir * self.speed * math.sin(rad) 
        self.dy = self.ydir * self.speed * math.cos(rad) 


    def move(self):
        self.center_x += self.dx
        self.center_y += self.dy


    def bounds_check(self):
        """
         checks ball for boundry conditions and collisions
         returns true if out of bounds
        """
        collision  = False
        player_out = False
        h2 = self.height / 2.0
        w2 = self.width / 2.0
        #  screen constraints
        TOP = const.SCREEN_HEIGHT - 1
        BOTTOM = 1
        LEFT = 1
        RIGHT = const.SCREEN_WIDTH - 1
        # check bounds
        if self.center_y >= TOP - h2:
            self.center_y = TOP - h2 - 1
            self.ydir *= -1
            collision = True  
            
        elif self.center_y <= BOTTOM + h2:
            self.center_y = 2 + h2 + BOTTOM
            self.ydir *= -1
            player_out = True
            collision  = True
                      
        if self.center_x >= RIGHT - w2:
            self.center_x = RIGHT - w2 - 1
            self.xdir *= -1
            collision = True
                      
        elif self.center_x <= LEFT+ w2:    
            self.center_x = 1 + w2 + LEFT
            self.xdir *= -1
            collision = True
        return collision, player_out    
    
    def update(self, paddle, bricks):
        collision, player_out = self.bounds_check()
        if player_out:
            # exit if player is out of  bounds
            self.dx = 0
            self.dy = 0
            return True
        elif collision: 
            Sounds.play_sound('wall-hit')
            self.update_dx_dy()
        # check for collision with paddle
        elif self.collides_with_sprite(paddle):
            Sounds.play_sound('paddle-hit')
            self.center_y = paddle.center_y + (paddle.height + self.height) / 2.0 + 1
            self.angle += rnd.triangular(20, 80) 
            self.ydir *= -1               
            self.update_dx_dy( )
        else:
            # check for collision with brickrray
            touched = self.collides_with_list(bricks)
            for brick in touched:
                if self.center_y > brick.bottom and self.center_y < brick.top: 
                    self.xdir *= -1
                else:
                    self.ydir *= -1
                self.update_dx_dy()        
                Sounds.play_sound('brick-hit-1')
                # add scoring
                brick.kill()
                # fix check for board cleared
        self.move()            
        return False
      
        
class Balls():
    def __init__(self, n = 1):
        self._balls = arcade.SpriteList(False)
        self.add_sprite(1)
        
        
    def add_sprite(self , n):
        for i in range(n):
            ball = BALL()      
            ball.createSprite(i)
            self._balls.append(ball)
            
            
    def home(self):
        if len(self._balls) < 1:
            self.add_sprite(1) 
        
    def update(self, paddle, bricks):
        # input paddle sprite and brick sprite list
        # output TRUE if last ball is out of bounds
        # otherwise False
        status = True
        dead = arcade.SpriteList(False)
        for ball in self._balls:
            state = ball.update(paddle, bricks)
            # if the ball is dead store it in the dead list
            if(state):
                dead.append(ball)
            status = status and state
        # delete all the dead balls    
        for ball in dead:
            ball.kill()    
        return status    

                
    def draw(self):
        self._balls.draw()