#!/usr/bin/python

from ctypes import *

libxdo = CDLL('libxdo.so.2')
xdo = libxdo.xdo_new(':0.0')

string = "abhishek"
print c_char_p(string)
libxdo.xdo_type(xdo, None, c_char_p(string), 100)
libxdo.xdo_keysequence(xdo, None, c_char_p("Return"), 100)
