#!/usr/bin/python

from ctypes import *
import sys
import socket

R_IP="0.0.0.0"
R_PORT=6003

r_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
r_sock.bind((R_IP, R_PORT))

libxdo = CDLL('libxdo.so.2')
xdo = libxdo.xdo_new(':0.0')

while True:
	data, addr = r_sock.recvfrom(1024)
	libxdo.xdo_type(xdo, None, c_char_p(data), 10)
