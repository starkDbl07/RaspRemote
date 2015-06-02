#!/usr/bin/python

import socket
from ctypes import *

r_addr = ('192.168.1.26', 6004)
r_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

r_sock.sendto("Return", r_addr)
