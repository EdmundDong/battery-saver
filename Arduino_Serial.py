#!/usr/bin/env python3
from time import sleep, strftime, localtime
import _thread as thread
import traceback
import random
import serial
import sys

def stamp():
    return strftime("%y-%m-%d %H:%M:%S GMT-7", localtime())

class Arduino_Serial:
    def __init__(self, port='/dev/ttyS4'):
       self.port = port
    def __enter__(self):
        # COM4 in Windows = /dev/ttyS4 in WSL
        self.conn = serial.Serial(self.port, 9600, timeout=0.1)
        if __name__ == '__main__':
            print('Connecting to Arduino...')
            thread.start_new_thread(self.__open_read__, ())
        sleep(2) # wait for connection
        return self

    def __open_read__(self):
        while self.conn.read(1000): # throw away garbage
            pass
        while True:
            message = self.conn.read(1000).decode().strip()
            if message == '1' or message == '0':
                message = "On Confirmed" if message == '1' else "Off Confirmed"
                print(f'{stamp()}: {message}')
    
    def send(self, data):
        self.conn.write(str(data).encode())
        sleep(2) # it takes about 2+-1 seconds for the data to reach the arduino

    def switch_on(self):
        self.send(1)
        if __name__ == '__main__':
            print(f'{stamp()}: On Sent')

    def switch_off(self):
        self.send(0)
        if __name__ == '__main__':
            print(f'{stamp()}: Off Sent')

    def __exit__(self, exc_type, exc_value, tb):
        self.conn.close()
        if exc_type is not None:
            traceback.print_exception(exc_type, exc_value, tb)
        return True

if __name__ == '__main__':
    relay = Arduino_Serial()
    while True:
        relay.switch_on()
        #print(relay.read())
        sleep(0.5)
        relay.switch_off()
        #print(relay.read())
        sleep(0.5)