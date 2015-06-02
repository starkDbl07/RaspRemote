#!/usr/bin/python

import cstdscr
import curses as cs
import socket
from ctypes import *
import sys
import os

r_mouse_addr = ('192.168.1.26', 6001)
r_click_addr = ('192.168.1.26', 6002)
r_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

stdscr = cstdscr.start()

#os.system("./netmouse.py &")

try:
    key = 0
    while (key != cs.KEY_F10):
        key = stdscr.getch()
        if ( key == 260):
            r_sock.sendto("1", r_click_addr)
        elif ( key == 261):
            r_sock.sendto("2", r_click_addr)
finally:
    cs.endwin()
