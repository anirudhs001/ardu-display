import datetime, threading, time
import getch

class Engine:
    pulseThread = threading.Thread
    inpThread

    def __init__(self):
        pulseThread = threading.Thread(target = self.pulse)
        inpThread = threading.Thread(target = self.cap_btn)
        self.btn_pressed = ''

    def start(self):
        self.pulseThread.start()
        self.inpThread.start()

    def pulse(self):
        next_call = time.time()
        while self.btn_pressed!= 'q':
            print(datetime.datetime.now()) 
            next_call = next_call + 1/2
            time.sleep(next_call - time.time())

    def cap_btn(self):
        self.btn_pressed = getch.getch()

if __name__ == "__main__":
    myengine = Engine
