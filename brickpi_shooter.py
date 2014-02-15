# -*- coding: UTF-8 -*- 
'''
Created on 15.02.2014

@author: jethroo
'''
###
import time

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

if __name__ == '__main__':
    import sys
    print ('Press a key')
    inkey = _Getch()
    while True:
        k=inkey()
        print(k[0])
        # 'a' turn left
        if (k[0] == 97):
            print('turning left');
            
        # 'd' turn right
        elif(k[0] == 100):
            print('turning right');
        
        # 'space' to shoot
        elif(k[0] == 32):
            print('ready aim fire....');
        
        # 'x' for closing
        elif(k[0] == 120):
            print('shooter is tired, shooter will sleep now, bye!');
            exit();
