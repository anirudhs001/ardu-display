import threading, time
import vga_serv
from vga_serv import game_engine
import getch
class sprite():
    
    def __init__(self, posn):
        if posn is not None:   
            self.x, self.y = posn
        else:
            self.x = 0; self.y = 0 


class Dino(sprite):

    def __init__(self):
        super.__init__()
        self.state = 'alive'

    def cntrl(self, cmd):
        if self.state is 'alive':
            if cmd is ' ' or 'k':
                self.jump()
            if cmd is 'j':
                self.crouch()

        elif self.state is 'dead':
            pass

    def jump(self):
        for i in range(0,10):
            self.y += -2 * i * (i - 10)
            time.sleep(vga_serv.frame_duration)


    def crouch(self):
        pass


def start():    
    dino = Dino()
    while not vga_serv.game_over:
        cmd = getch.getch()
        dino.cntrl(cmd)


if __name__ == "__main__":
    threading.Thread(target=start).start()
    game_engine.main