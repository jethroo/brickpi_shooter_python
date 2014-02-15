# -*- coding: UTF-8 -*-
'''
Created on 15.02.2014

@author: jethroo
'''
###

from BrickPi import * #import BrickPi.py file to use BricPi operations
import time
import threading
import struct
import sys

class _Getch:
    """Gets a single character from standard input.  Does not echo to the screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self):
        bytes = self.impl()
        if bytes == b'\x03':
            raise KeyboardInterrupt
        elif bytes == b'\x04':
            raise EOFError
        return bytes

class _GetchUnix:
    def __init__(self):
        import tty
        import sys

    def __call__(self):
        import sys
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()


def turn_left():
    print('turning left');
    BrickPi.MotorSpeed[PORT_A] = 0
    BrickPi.MotorSpeed[PORT_D] = 100
    update_and_wait()

def turn_right():
    print('turning right');
    BrickPi.MotorSpeed[PORT_A] = 0
    BrickPi.MotorSpeed[PORT_D] = -100
    update_and_wait()

def shoot():
    print('ready aim fire....');
    BrickPi.MotorSpeed[PORT_A] = 400
    BrickPi.MotorSpeed[PORT_D] = 0
    update_and_wait()

def update_and_wait():
    BrickPiUpdateValues();
    time.sleep(0.1)

if __name__ == '__main__':

    BrickPiSetup() #setup the serial port for communication
    BrickPi.MotorEnable[PORT_A] = 1 #Enable the Motor A
    BrickPi.MotorEnable[PORT_D] = 1 #Enable the Motor D
    BrickPiSetupSensors() #Send the properties of sensors to BrickPi

    print ('Press a key')
    inkey = _Getch()
    while True:
        k=inkey()
        print(k[0])
        # 'a' turn left ord: 97
        if (k[0] == 'a'):
            turn_left();
        # 'd' turn right ord: 100
        elif(k[0] == 'd'):
            turn_right();
        # 'space' to shoot ord: 32
        elif(k[0] == ' '):
            shoot();
        # 'x' for closing ord: 120
        elif(k[0] == 'x'):
            print('shooter is tired, shooter will sleep now, bye!');
            exit();
