import threading, time

import vga_serv.server as server 
import vga_serv.game_engine as game_engine
import vga_serv

import random

random.seed(time.time())

#CONSTANTS:
#   -> constants for 120x60 px screen
DINO_WIDTH = 3
DINO_HEIGHT = 4
JUMP_SCALE = 0.8
OBSTACLE_WIDTH = 3
OBSTACLE_HEIGHT = 4
OBSTACLE_SEPERATION = 20
NUM_OBSTACLES = 2
STEP = 5

class Obstacle():
    def __init__(self, last_sprites_x, id):
        #initialize obstacle 
        # current obstacle is some distance behiqnd the last obstacle and also outside screen width 
        self.step = STEP
        self.x = ( max(vga_serv.frame_width, last_sprites_x) + 
                 random.randint( OBSTACLE_SEPERATION, vga_serv.frame_width) % self.step)
        self.y = 0
        self.width = OBSTACLE_WIDTH
        self.height = OBSTACLE_HEIGHT
        self.dino_width = DINO_WIDTH
        self.stance = 0
        self.id = id #TODO: change if more than one type of obstacles

    def killed_dino(self, dino_x, dino_y):
        if dino_x in range(self.x - self.dino_width, self.x + self.width + 1) and dino_y in range(self.y - DINO_HEIGHT , self.y + self.height + 1):
            return True
        return False    

    def move(self, dino_x, dino_y, last_sprites_x):
        if self.killed_dino(dino_x, dino_y):
            vga_serv.game_over = True #TODO: change to true if obstacle kills dino
        if self.x <= 0:
            self.reset(last_sprites_x)   
        else:
            self.x -= self.step
        game_engine.update_sprite(self)

    def reset(self, last_sprites_x):
        self.x = ( max(vga_serv.frame_width, last_sprites_x) + 
                 random.randint( OBSTACLE_SEPERATION, vga_serv.frame_width))
    
        

class ArmyObstacles():
    def __init__(self):
        #create army of obstacles
        self.arr = [Obstacle(0, idx) for idx in range(0,NUM_OBSTACLES)]
        for i in range(1, NUM_OBSTACLES):
            self.arr[i].reset(self.arr[i - 1].x)

    def move(self, dino_x, dino_y):
        for i in range(0, NUM_OBSTACLES):
            if i == 0:
                self.arr[i].move(dino_x, dino_y, last_sprites_x = self.arr[NUM_OBSTACLES - 1].x)
            else:
                self.arr[i].move(dino_x, dino_y, last_sprites_x = self.arr[i - 1].x)
                

class Dino():
    def __init__(self):
        self.state = 'alive'
        self.action = 'walk'
        self.x = 0
        self.y = 0
        self.width = 8
        self.height = 8
        self.stance = 0
        self.jump_scale = JUMP_SCALE
        self.id = 'D'
        self.i = 0  #counter to hold current jumping position
        #stance is defined as: 0 == walking_1
        #                      1 == walking_2
        #                      2 == crouched
    def cntrl(self, cmd):
        if self.state == 'alive':
            if cmd == ' ' or cmd == 'k':
                self.jump()
            if cmd == 'j':
                self.crouch()
            else:
                self.straight()
        elif self.state == 'dead':
            pass

    def straight(self):
        if self.action == 'walk':
            self.stance = (self.stance + 1) % 2  
        elif self.action == 'jump':
            self.jump()
        elif self.action == 'crouch':
            self.action = 'walk'
        game_engine.update_sprite(self)

    def jump(self):
        if self.action == 'crouch':
            self.action = 'crouch' #cant jump while crouching
        elif self.action == 'walk':
            self.action = 'jump'
            self.i = 0
            self.jump()
        elif self.action == 'jump':
            #jump in a parabola:
            self.y = int(-self.jump_scale * self.i * (self.i - 10)) #TODO: make the algo for jumping more readable
            self.i += 1
            if self.i > 10:
                self.action = 'walk'
                self.i = 0
        game_engine.update_sprite(self)

    def crouch(self):
        if self.action == 'jump':
            self.i = 0
            self.y = 0
        self.action = 'crouch'
        self.stance = 2
        game_engine.update_sprite(self)
    

def run_game():    
    while not vga_serv.game_over:
        #update obstacle's pos:
        army.move(dino.x, dino.y)
        #update dino's posn 
        cmd = game_engine.get_inp()
        if cmd:
            print(f"{__name__}: got input<{cmd}>") 
            if cmd.lower() == 'q':
                print(f"{__name__}: exiting... ")
                vga_serv.game_over = True
        dino.cntrl(cmd)
        time.sleep(vga_serv.frame_duration)
    game_engine._close()
    print(f"{__name__}: game engine shut down...")


if __name__ == "__main__":

    print(f"{__name__}: game started! press any key:")
    #object of class dino
    dino = Dino()
    #objects of class Obstacle
    army = ArmyObstacles() 

    print(f"{__name__}: game running...")
    game_engine.start_engine()
    print(f"{__name__}: [threads running: {threading.enumerate()}]")

    run_game() #not running on a thread; so main thread executes the next line when run_game exits
    #print all running threads:
    print(f"{__name__}: [threads running: {threading.enumerate()}]")