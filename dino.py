import threading, time
import sys

import vga_serv.server as server 
import vga_serv.game_engine as game_engine
import vga_serv
import readchar

class Dino():

    def __init__(self, id):
        self.state = 'alive'
        self.id = id
        self.x = 0
        self.y = 0

    def cntrl(self, cmd):
        if self.state == 'alive':
            if cmd == ' ' or cmd == 'k':
                self.jump()
            if cmd == 'j':
                self.crouch()

        elif self.state == 'dead':
            pass

    def jump(self):
        for i in range(0,10):
            self.y += -2 * i * (i - 10)
            game_engine.update_sprite(self.id, self.x, self.y)
            time.sleep(0.1)
            

    def crouch(self):
        pass


def start_dino():    
    while not vga_serv.game_over:
        try:
            cmd = readchar.readchar()# TODO: fix this.records single key but badly formats the output
            if cmd is not None:
                print(f"{__name__}: key <{cmd}> recorded!")
                dino.cntrl(cmd)
        except KeyboardInterrupt:
            vga_serv.game_over = True
   
        time.sleep(vga_serv.frame_duration)
    
    for thread in threading.enumerate():
        thread.join()
        thread.exit()

if __name__ == "__main__":

    print(f"{__name__}: game started! press any key:")
    #object of class dino
    dino = Dino('dino')
    #start game
    thread_1 = threading.Thread(target=start_dino)
    thread_1.start()

    print(f"{__name__}: game running...")
    game_engine.start_engine()

    #print all running threads:
    print(f"{__name__}: [threads running: {threading.enumerate()}]")