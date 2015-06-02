#!/usr/bin/python

from ctypes import *
import sys
import socket

R_IP="0.0.0.0"
R_PORT=6001

r_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
r_sock.bind((R_IP, R_PORT))

libxdo = CDLL('libxdo.so.2')
xdo = libxdo.xdo_new(':0.0')

cur_x, cur_y, cur_screen, cur_window = c_int(), c_int(), c_int(), c_int()

while True:
	data, addr = r_sock.recvfrom(1024)
	dnd_x = int(data.split(" ")[0])
	dnd_y = int(data.split(" ")[1])
	libxdo.xdo_mouselocation(xdo, byref(cur_x), byref(cur_y), byref(cur_screen))
	libxdo.xdo_mousemove(xdo, dnd_x, dnd_y, cur_screen)
