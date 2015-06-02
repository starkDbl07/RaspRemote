#!/usr/bin/python

import socket
import subprocess
from ctypes import *

r_addr = ('192.168.1.26', 6001)
r_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#libxdo = CDLL('libxdo.so.2')
#xdo = libxdo.xdo_new(':0.0')
#cur_x, cur_y, cur_screen, cur_window = c_int(), c_int(), c_int(), c_int()

while True:
    mouseloc = subprocess.check_output(["./MouseLocation"])
    #libxdo.xdo_mouselocation(xdo, byref(cur_x), byref(cur_y), byref(cur_screen))
    r_sock.sendto(str(cur_x) + " " + str(cur_y), r_addr)
