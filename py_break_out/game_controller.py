# game controller module
# k.r.bergerstock @ oct,2020

from time import sleep
import pyglet.input

def __convert__(value):
    if value > 0.6:
        return 1
    elif value < -0.6:
        return -1
    else:
        return 0  

class game_controller:
    def __init__(self, idx):
        self.jss = None
        self.js = None
        self.Setup(idx)

    def Setup(self, js):
        self.jss = pyglet.input.get_joysticks()
        if self.jss:
            self.js = self.jss[js]
            self.js.open()

    def buttonX(self):
        return False if not self.js else self.js.buttons[0]

    def buttonA(self):
        return False if not self.js else self.js.buttons[1]

    def buttonB(self):
        return False if not self.js else self.js.buttons[2]

    def buttonY(self):
        return False if not self.js else self.js.buttons[3]

    def axisX(self):
        return False if not self.js else __convert__(self.js.x) 
    
if __name__ == "__main__":
    ji = game_controller(0)
    print(ji.jss, ji.js )
    for i in range(259):
        print(ji.js.buttons)
        sleep(.10)
     
