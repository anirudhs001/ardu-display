from threading import Thread, Event
import getch


class MainThread(Thread):
    
    def __init__(self, event):
        Thread.__init__(self)
        self.stopped = event
        
        #thread to record button presses:
        stop_btn_capture = Event()
        inp_thread = Inp_Thread(stop_btn_capture)
        inp_thread.start()

    def run(self):
        while not self.stopped.wait(0.5):
            #TODO: update Frame
            pass 

class Inp_Thread(Thread):

    def __init__(self, event):
        Thread.__init__(self)
        self.stopped = event
        
def main():
    #create thread to start game:
    stopFlag = Event()
    game_thread = MainThread(stopFlag)
    game_thread.start()
    

if __name__ == "__main__":
    main()
