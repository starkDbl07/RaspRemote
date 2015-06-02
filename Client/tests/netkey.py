#!/usr/bin/python

import socket
from ctypes import *

r_addr = ('piabhi.local.', 6004)
r_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

r_sock.sendto("ctrl+c", r_addr)
