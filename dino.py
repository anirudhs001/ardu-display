import threading, time

import vga_serv.server as server 
import vga_serv.game_engine as game_engine
import vga_serv

import random

random.seed(time.time())

#CONSTANTS:
DINO_WIDTH = 0
DINO_HEIGHT = 20
OBSTACLE_WIDTH = 0
OBSTACLE_HEIGHT = 0
STEP = 10

class Obstacle():
    def __init__(self, last_sprites_x, dino_width):
        #initialize obstacle 
        # current obstacle is some distance behind the last obstacle and also outside screen width 
        self.x = ( max(vga_serv.frame_width, last_sprites_x) + 
                 random.randint(1.5 * dino_width, vga_serv.frame_width / 2))
        self.y = 50
        self.width = 8
        self.height = 8
        self.dino_width = dino_width
        self.step = 1
        self.stance = 0

    def killed_dino(self, dino_x, dino_y):
        if dino_x in range(self.x - self.dino_width, self.x + self.width) and dino_y in range(self.y , self.y + self.height):
            return True
        return False    

    def move(self, dino_x, dino_y):
        if self.killed_dino(dino_x, dino_y):
            vga_serv.game_over = True
        elif self.x <= 0:
            self.reset(last_sprites_x = 0) #TODO: update last_sprites_x if more than one obstacles in game
        else:
            self.x -= self.step
        #TODO: send current posn and stance to game engine

    def reset(self, last_sprites_x):
        self.__init__(last_sprites_x, self.dino_width)
        
        
class Dino():
    def __init__(self):
        self.state = 'alive'
        self.x = 0
        self.y = 0
        self.width = 8
        self.height = 8
        self.stance = 0
        self.id = "dino"
        #stance is defined as: 0 == walking_1
        #                      1 == walking_2
        #                      2 == crouched
    def cntrl(self, cmd):
        if self.state == 'alive':
            if cmd == ' ' or cmd == 'k':
                self.jump()
            if cmd == 'j':
                self.crouch()
            if cmd is None:
                self.straight()
        elif self.state == 'dead':
            pass

    def straight(self):
        self.stance = (self.stance + 1) % 2
        self.y = 0
        game_engine.update_sprite(self)

    def jump(self):
        for i in range(0,11):
            self.y = int(-i * (i - 10))
            game_engine.update_sprite(self)
            time.sleep(vga_serv.frame_duration)
            game_engine.update_sprite(self)
        

    def crouch(self):
        self.stance = 2
        game_engine.update_sprite(self)


def run_game():    
    while not vga_serv.game_over:
        #update obstacle's pos:
        obstacle.move(dino.x, dino.y)
        #update dino's posn 
        try:
            cmd = game_engine.getch()
            if cmd.lower() != 'q':
                print(f"{__name__}: key <{cmd}> recorded!")
                dino.cntrl(cmd)
            elif cmd.lower() == 'q':
                vga_serv.game_over = True
        except KeyboardInterrupt:
            vga_serv.game_over = True

        time.sleep(0.1)#TODO: change time to frame duration
    game_engine._close()
    print(f"{__name__}: exiting...")


if __name__ == "__main__":

    print(f"{__name__}: game started! press any key:")
    #object of class dino
    dino = Dino()
    #object of class Obstacle
    obstacle = Obstacle(last_sprites_x = 0,dino_width = dino.width)

    #start game
    thread_1 = threading.Thread(target=run_game)
    thread_1.start()

    print(f"{__name__}: game running...")
    game_engine.start_engine()

    #print all running threads:
    print(f"{__name__}: [threads running: {threading.enumerate()}]")