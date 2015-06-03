#!/usr/bin/python

import cstdscr
import curses as cs
import socket
from ctypes import *
import sys
import os

r_host = 'raspberrypi.local.'
r_addr_pointer = 6001
r_addr_click = 6002
r_addr_type = 6003
r_addr_key = 6004

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

appTitleHeight = 10
stdscr = cstdscr.start()
keydown = 0

windows = {'appTitle':None, \
            'rContent':None }
windows_dimen = None
appTitle = "CRaspRemote - Terminal Raspberry Remote"
#appMenus = [ "[F10] Enable Mouse Move", "[F11] Switch To Mouse Click", "[F12] Switch To Keyboard"]
appMenus = [ "[F11] Switch To Mouse", "[F12] Switch To Keyboard"]
appMenuLeft = 30

cs.init_pair(1,cs.COLOR_BLACK,cs.COLOR_WHITE)
cs.init_pair(2,cs.COLOR_BLACK,cs.COLOR_GREEN)

attrs = {'appTitleWindow': cs.A_STANDOUT, \
            'appTitle': cs.A_STANDOUT | cs.A_BOLD, \
            'topMenuItem': cs.color_pair(1), \
        }

def reset_windows_dimens():
    global windows_dimen
    windows_dimen = {'appTitle':(appTitleHeight,cs.COLS,0,0), \
                    'rContent':(cs.LINES-appTitleHeight,cs.COLS,appTitleHeight,0)}
        
def place_windows():
    for window in windows.keys():
        wHeight, wWidth, wStartY, wStartX = windows_dimen[window]
        windows[window] = stdscr.subwin(wHeight, wWidth, wStartY, wStartX)
        windows[window].box()
        windows[window].noutrefresh()
    cs.doupdate()

def draw_window_apptitle():
    window = windows['appTitle']
    window.clear()
    window.bkgd(" ", attrs['appTitleWindow'])
    window.addstr(1, (cs.COLS/2) - (len(appTitle)/2), appTitle, attrs['appTitle'])
    window.noutrefresh()
    cs.doupdate()

def draw_window_menu():
    quitItem = "[F9] Quit"
    window = windows['rContent']
    window.clear()
    window.bkgd(" ", attrs['appTitleWindow'])
    window.addstr(1, (cs.COLS/2) - (len(quitItem)/2), quitItem, attrs['topMenuItem'] | cs.A_BOLD)
    for y in range(0,len(appMenus)):
        window.addstr((y*2) + y+4, (cs.COLS/2) - (len(appMenus[y])/2), appMenus[y], attrs['topMenuItem'])

    window.noutrefresh()
    cs.doupdate()

def redraw_all():
    reset_windows_dimens()
    stdscr.clear()
    stdscr.bkgd(" ", attrs['appTitleWindow'])
    place_windows()
    draw_window_apptitle()
    draw_window_menu()


def set_mousepointer(mousepointer=True):
    #stdscr.addstr("toggle_pointer")
    if ( mousepointer ):
        os.system("./mousestart.sh >/dev/null 2>&1 &")
    else:
        os.system("./mouseend.sh >/dev/null 2>&1 &")

def start_click():
    #stdscr.addstr("start_click")
    global key
    windows['rContent'].chgat(4,0,cs.color_pair(2) | cs.A_STANDOUT)
    windows['rContent'].chgat(7,0,attrs['topMenuItem'] | cs.A_STANDOUT)
    windows['rContent'].noutrefresh()
    cs.doupdate()
    set_mousepointer(True)
    while True:
        key = stdscr.getch()
        if ( key >= 273 and key <= 276 ):
            break
        elif ( key == 260):
            r_sock.sendto("1", (r_host, r_addr_click))
        elif ( key == 261):
            r_sock.sendto("2", (r_host, r_addr_click))

def start_keyboard():
    #stdscr.addstr("start_keyboard")
    global key
    windows['rContent'].chgat(4,0,attrs['topMenuItem'] | cs.A_STANDOUT)
    windows['rContent'].chgat(7,0,cs.color_pair(2) | cs.A_STANDOUT)
    windows['rContent'].noutrefresh()
    cs.doupdate()
    set_mousepointer(False)
    while True:
        key = stdscr.getch()
        if ( key >= 32 and key <= 126 ): 
            r_sock.sendto(chr(key), (r_host, r_addr_type))
        elif ( key >= 273 and key <= 276 ):
            break
        else:
            try:
                #stdscr.addstr(str(int(key)))
                r_sock.sendto(xdo_keymaps[key], (r_host, r_addr_key))
            except:
                pass
    #check_functionkey(key)

def exiting():
    cstdscr.end()
    print "Exiting..."
    os.system("./mouseend.sh >/dev/null 2>&1 &")
    sys.exit()

def check_functionkey(key):
    function_keymaps[key]()


function_keymaps={275: start_click, 276: start_keyboard, 273: exiting}
stdscr = cstdscr.start()
redraw_all()

try:
    key = stdscr.getch()
    while True:
        if ( key >= 273 and key <= 276 ):
            check_functionkey(key)
finally:
    exiting()
