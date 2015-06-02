#!/usr/bin/python

import socket
from ctypes import *
import sys

r_addr = ('192.168.1.26', 6003)
r_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

r_sock.sendto(sys.argv[1], r_addr)
