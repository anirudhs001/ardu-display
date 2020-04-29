from bitarray import bitarray
import serial
import time

import vga_serv

class VGA:

    def __init__(self):
        self.WIDTH = 180#?
        self.HEIGHT = 192#?
        self.ser = serial.Serial(vga_serv.port, 115200, timeout=vga_serv.frame_duration) 
        self.sprite_list = ['dino']        
        self.sprite_posn = { x:(0,0) for x in self.sprite_list }
        
    def update_sprite(self, x, y, id):
    #update the posn of sprite to send to the arduino
        self.sprite_posn[id] = (x,y)
        
    def flush_frame(self):
    #send posn of all sprites to arduino.
    #format: sprite_id (x,y)
        for sprite in self.sprite_list:
            self.ser.write(sprite.encode())
            self.ser.write(self.sprite_posn[sprite])
            print(f"{__name__}: {sprite} flushed" )
        

