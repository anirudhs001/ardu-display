import threading
import getch
import time
import vga_serv
import serial
import asyncio

class Engine(threading.Thread):

    def __init__(self):
        super(Engine, self).__init__()
        self.running = True
        self.sleep_time = 0.1
        
    #run is a member func of class Thread, started when thread.start() is called
    # use here: 1)send the posn of sprites to arduino
    #           2)checks usr input  
    def run(self, arduino):
        while self.running:
            #send data to arduino
            with serial.Serial(vga_serv.port, 115200, timeout=0.1) as ser:
                arduino = vga_serv.VGA()

                arduino.flush_frame(ser)
                time.sleep(self.sleep_time)



def main():
    myengine = Engine
    Engine.start(myengine)
    while myengine.running:
        try:
            resp = getch.getch()
            


if __name__ == "__main__":
    