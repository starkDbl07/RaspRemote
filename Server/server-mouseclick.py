#!/usr/bin/python

from ctypes import *
import sys
import socket

R_IP="0.0.0.0"
R_PORT=6002

r_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
r_sock.bind((R_IP, R_PORT))

libxdo = CDLL('libxdo.so.2')
xdo = libxdo.xdo_new(':0.0')

while True:
	data, addr = r_sock.recvfrom(1)
	libxdo.xdo_click(xdo, None, int(data))
