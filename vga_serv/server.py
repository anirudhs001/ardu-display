from bitarray import bitarray
import serial
import time


class VGA:

    def __init__(self):
        self.WIDTH = 180#?
        self.HEIGHT = 192#?
        self.canvas = bitarray(self.WIDTH * self.HEIGHT)
        self.canvas[:] = False
        
    def add_sprite(self, x, y, arr, w, h):
    #x and y are the coords of the top-left corner of sprite
    #the canvas is drawn in the 3rd coord(but with +ve x and y)
        for i in range(0, h):
            self.canvas[ y*self.WIDTH + x : y*self.WIDTH + x+w] = arr[i][:]

    def flush_frame(self, ser):
    #send the frame ( a 'bytearray' via serial to the arduino)
    #currently canvas is stored as bit array but pyserial can 
    #only write bytearrays...
    #TODO :convert bytearray in *arduino* to bit array
        #send a big byte array to arduino and check the time
        ser.write(b"123456")
        print(str(ser.readline()))


if __name__ == "__main__":
    main()
    