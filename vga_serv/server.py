from bitarray import bitarray
import serial
import time

import vga_serv

class VGA:

    def __init__(self):
        self.WIDTH = 180#?
        self.HEIGHT = 192#?
        try:
            self.ser = serial.Serial(vga_serv.port, 9600, timeout=vga_serv.frame_duration) 
            print(f"{__name__}: Serial connection started!")
        except:
            print(f"{__name__}: could not start serial comm!")

    #update the posn of sprite to send to the arduino
    # x and y are the coords of the bottom left corner(frame is drawn in 1st quadrant)
        
    def flush_frame(self, sprites_dict):
    #send posn of all sprites to arduino.
    #format: sprite-id_stance_x_y
        try:
            for s in sprites_dict:
                #send sprite as :name_stance_x_y
                num_bytes = self.ser.write(f"{s}_{sprites_dict[s][0]}_{sprites_dict[s][1]}_{sprites_dict[s][2]}|".encode())
                # self.ser.write("ani_rudh_".encode())
                print(f"{__name__}: {s}:{sprites_dict[s]} flushed. {num_bytes} bytes written" )
        except :
            "could not write! :("
