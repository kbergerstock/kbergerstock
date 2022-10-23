import const
import arcade

class Sounds():
    snds = {}
    
    @classmethod
    def load(cls):
        # load the sounds
        cls.snds['music']  = arcade.Sound('resources/music.wav',True)
        cls.snds['victory'] = arcade.Sound('resources/victory.wav')
        cls.snds['select'] = arcade.Sound('resources/select.wav')
        cls.snds['no-select'] = arcade.Sound('resources/no-select.wav')
        cls.snds['confirm'] = arcade.Sound('resources/confirm.wav')
        cls.snds['wall-hit'] = arcade.Sound('resources/wall_hit.wav')
        cls.snds['paddle-hit'] = arcade.Sound('resources/paddle_hit.wav')
        cls.snds['pause'] = arcade.Sound('resources/pause.wav')
        cls.snds['score'] = arcade.Sound('resources/score.wav')
        cls.snds['brick-hit-1'] = arcade.Sound('resources/brick-hit-1.wav')
        cls.snds['brick-hit-2'] = arcade.Sound('resources/brick-hit-2.wav')
        cls.snds['high_score'] = arcade.Sound('resources/high_score.wav')
        cls.snds['recover'] = arcade.Sound('resources/recover.wav')
        
        # create the game controller interface
        cls.snds['music'].play(const.VOLUME)
    
    @classmethod
    def play_sound(cls, sound):
        cls.snds[sound].play(const.VOLUME)