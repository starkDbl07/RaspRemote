#!/usr/bin/python

import cstdscr
import curses as cs
import socket
from ctypes import *
import sys

r_type_addr = ('192.168.1.26', 6003)
r_key_addr = ('192.168.1.26', 6004)
r_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

xdo_keymaps={127: 'BackSpace', \
            10: 'Return', \
            258: 'Down', \
            259: 'Up', \
            260: 'Left', \
            261: 'Right', \
            330: 'Delete', \
            9: 'Tab', \
            100 : 'Space', \
            27: 'Escape', \
            167: 'ctrl+c', \
        }

stdscr = cstdscr.start()

try:
    key = 0
    while (key != cs.KEY_F10):
        key = stdscr.getch()
        if ( key == cs.KEY_MOUSE):
            a, mx, my, mz, c = cs.getmouse()
            stdscr.addstr(10,10, str(mx) + "," + str(my))
        elif ( key >= 32 and key <= 126 ): 
            r_sock.sendto(chr(key), r_type_addr)
        else:
            try:
                stdscr.addstr(str(int(key)))
                r_sock.sendto(xdo_keymaps[key], r_key_addr)
            except:
                pass
finally:
    cs.endwin()
