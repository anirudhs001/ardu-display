from vga_serv import server


class sprite:
    
    def __init__(self, posn):
        if posn is not None:   
            self.x, self.y = posn
        else:
            self.x = 0; self.y = 0 


class dino:

    def __init__(self):
        self.state = 'alive'

    def cntrl(self, cmd):
        if self.state is 'alive':
            if cmd is ' ' or 'k':
                self.jump()
            if cmd is 'j':
                self.crouch()

        elif self.state is 'dead':
            self.dead()

    def jump(self):
        for i in range()    

    