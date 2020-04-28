import threading
import getch
import time
import serial
import asyncio
import vga_serv

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
                arduino.add_response(resp)
                arduino.flush_frame(ser)
                time.sleep(self.sleep_time)



def start():
    myengine = Engine
    Engine.start(myengine)
    global resp
    resp = ''
    while myengine.running:
        try:
            resp = getch.getch()
            
        except: KeyboardInterrupt
    myengine.running = False


if __name__ == "__main__":
    main()