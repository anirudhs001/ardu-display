from bitarray import bitarray
import serial
import time

import vga_serv

class VGA:

    def __init__(self):
        self.WIDTH = 180#?
        self.HEIGHT = 192#?
        try:
            self.ser = serial.Serial(vga_serv.port, 115200, timeout=vga_serv.frame_duration) 
            print(f"{__name__}: Serial connection started!")
        except:
            print(f"{__name__}: could not start serial comm!")

    #update the posn of sprite to send to the arduino
    #x and y are the coord of bottom left corner of sprite
        
    def flush_frame(self, sprites_dict):
    #send posn of all sprites to arduino.
    #format: sprite_id (x,y)
        try:
            for sprite in sprites_dict:
                #send sprite as :name_stance_x_y
                self.ser.write(f"{sprite.x}_{sprite.y}_".encode())
                # self.ser.write("ani_rudh_".encode())
                print(f"{__name__}: {sprite} flushed" )
        except :
            "could not write! :("
