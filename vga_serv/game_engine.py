import threading
import getch
import time
import serial
import vga_serv.server as server
import vga_serv


global arduino 
arduino = server.VGA()
class Engine(threading.Thread):

    def __init__(self):
        super(Engine, self).__init__()
        self.sleep_time = vga_serv.frame_duration
        self.running = True 

    def run(self):
    #run is a member func of class Thread, started when thread.start() is called
    # use here: 1)send the posn of sprites to arduino
    #           2)checks usr input  
    #send data to arduino
        while self.running:
            #arduino.flush_frame()
            print(f'{__name__}:frame updated!')
            time.sleep(self.sleep_time)


def update_sprite(id, x, y):
    arduino.update_sprite(id, x, y)

def start_engine():
    print(f'{__name__}: vga server created')

    myengine = Engine()
    Engine.start(myengine)

    print(f'{__name__}: engine started')   


if __name__ == "__main__":
    start_engine()