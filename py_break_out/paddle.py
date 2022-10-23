#paddle.py

import arcade
import const

class PADDLE(arcade.Sprite):
    def __init__(self):
        super().__init__() 
        self.textures = arcade.load_textures(const.PADDLE_TEXTURES,const.PADDLE_LOCATIONS)
        self.speed = const.PADDLE_VELOCITY
        self.scale = const.PADDLE_SCALE
        self.texture_idx = 0
        self.createSprite()


    def createSprite(self):
        for i in range(16):
            self.append_texture(self.textures[i])
        self.set_position(600,40)
        self.set_texture(1)

    def home(self):
         self.set_position(600,40)

    def set_texture(self, idx):
        self.texture_idx = idx
        super().set_texture(idx)    


    def update(self, dt, direction):    
        pos = self.center_x + self.speed * dt * direction
        if not (pos <= self.width / 2 or pos >= const.SCREEN_WIDTH - self.width / 2):
            self.center_x = pos


    def inc_texture(self):
        if self.texture_idx < 12:
            self.set_texture(self.texture_idx + 4)


    def dec_texture(self):
        if self.texture_idx >= 4:
            self.set_texture(self.texture_idx - 4)
