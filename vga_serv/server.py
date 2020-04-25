from bitarray import bitarray
import serial

ser = serial.Serial()
ser.port = 'COM2'

class VGA:

    def __init__(self):
        self.WIDTH = 180#?
        self.HEIGHT = 192#?
        self.canvas = bitarray(self.WIDTH * self.HEIGHT)
        self.canvas[:] = False
        
    #x and y are the coords of the top-left corner of sprite
    #the canvas is drawn in the 3rd coord(but with +ve x and y)
    def add_sprite(self, x, y, arr, w, h):
        for i in range(0, h):
            self.canvas[ y*self.WIDTH + x : y*self.WIDTH + x+w] = arr[i][:]

    #send the frame ( a 'bytearray' via serial to the arduino)
    #currently canvas is stored as bit array but pyserial can 
    #only write bytearrays...
    #TODO :convert bytearray in *arduino* to bit array
    def flush_frame(self):
        ser.write(bytearray(self.canvas))