import threading
import getch
import time
import vga_serv

class Engine(threading.Thread):

    def __init__(self):
        super(Engine, self).__init__()
        self.running = True
        
    #run is a member func of class Thread, started when thread.start() is called
    # use here: 1)send the posn of sprites to arduino
    #           2)checks usr input  
    def run(self, arduino):
        while self.running:
            #send data to arduino
            with serial.Serial(vga_serv.port, 115200, timeout=0.1) as ser:
                arduino = VGA()
                

    def cap_btn(self):
        self.btn_pressed = getch.getch()


#repeat a func repeatitively:
def thread_funcn():
    #mimic sending data to arduino
    time.sleep(2)



def main():

    with serial.Serial('/dev/ttyACM0', 115200, timeout = 0.1) as ser:
        arduino = VGA()

        start_time = time.time()
        arduino.flush_frame(ser)
        end_time = time.time()
        
        print(f"time taken = {end_time - start_time}")

if __name__ == "__main__":
    myengine = Engine
    Engine.start(myengine)