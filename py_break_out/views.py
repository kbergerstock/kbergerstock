# break ouy : views .py
# k.r.bergerstock
# 10/20/2022

import const
import arcade
from start_view  import startView      
from select_view import selectView
from serve_view  import serveView
from level_view  import levelView


class Views():
    def __init__(self):
        # create the game views
        self._start_view  = None 
        self._select_view = None
        self._serve_view  = None
        self._level_view  = None
        # window handle
        self._window = None

        
    def SelectView(self, view):
        if view == 'start_view':
            self._window.show_view(self._start_view)
        elif view == 'select_view':
            self._window.show_view(self._select_view)
        elif view == 'serve_view':
            self._window.show_view(self._serve_view)
        elif view == 'level_view':
            self._window.show_view(self._level_view)
        else:
            # fix
            pass    
        arcade.set_viewport(0,const.SCREEN_WIDTH,5,const.SCREEN_HEIGHT-5)

        
    def load(self, game):
        self._window = arcade.Window(const.SCREEN_WIDTH,const.SCREEN_HEIGHT-10, const.SCREEN_TITLE)
        arcade.set_viewport(0,const.SCREEN_WIDTH,5,const.SCREEN_HEIGHT-5)
        # create the game views
        # store a refence to each view
        self._start_view  = startView(game, self.SelectView)
        self._select_view = selectView(game, self.SelectView)
        self._serve_view  = serveView(game, self.SelectView)
        self._level_view  = levelView(game, self.SelectView)
        self.SelectView('start_view')
        
        