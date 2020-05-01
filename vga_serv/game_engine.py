import threading
import time
import vga_serv.server as server
import vga_serv
import sys

global arduino 
arduino = server.VGA()

def get_getch():
    try:
        import msvcrt
        if sys.version_info.major == 2:
            return msvcrt.getch
        else:
            return lambda : msvcrt.getch().decode('utf-8')
    except ImportError:
        return lambda : sys.stdin.read(1)

getch = get_getch()
class Console(object):

    @staticmethod
    def init():
        try:
            import termios
            Console.is_unix = True
            Console.fd = sys.stdin.fileno()
            Console.oldattr = termios.tcgetattr(Console.fd)
            newattr = termios.tcgetattr(Console.fd)
            newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
            termios.tcsetattr(Console.fd, termios.TCSANOW, newattr)
        except ImportError:
            Console.is_unix = False

    @staticmethod
    def reset():
        if Console.is_unix:
            import termios
            termios.tcsetattr(Console.fd, termios.TCSANOW, Console.oldattr)

Console.init()

#basic sprite class to hold posns and stance
class sprite():
    def __init__(self, s):
        self.x = s.x
        self.y = s.y
        self.width = s.width
    

class Engine(threading.Thread):

    def __init__(self):
        super(Engine, self).__init__()
        self.sleep_time = vga_serv.frame_duration
        vga_serv.game_over = False 
        self.sprites_dict = {} 

    def run(self):
    #run is a member func of class Thread, called on thread.start() 
    # use here: 1)send the posn of sprites to arduino
    #           2)checks usr input  
    #send data to arduino
       while not vga_serv.game_over:
            arduino.flush_frame(self.sprites_dict)
            print(f'{__name__}:frame updated!')
            time.sleep(self.sleep_time)

    def _close(self):
        Console.reset()
        print("shutting down game engine...")
        
myengine = Engine()

def _close():
    myengine._close()

def update_sprite(s):
    myengine.sprites_dict[s] = (s.stance, s.x, s.y)

def start_engine():
    print(f'{__name__}: vga server created')

    Engine.start(myengine)

    print(f'{__name__}: engine started')   


if __name__ == "__main__":
    start_engine()