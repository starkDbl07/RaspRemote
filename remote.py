#!/usr/bin/python

import cstdscr
import curses as cs
stdscr = cstdscr.start()

try:
    stdscr.addstr("test")
    
    key = 0
    while (key != cs.KEY_F10):
        a, mx, my, mz, c = cs.getmouse()
        stdscr.addscr(10,10, str(mx) + "," + str(my))
        key = stdscr.getch()

finally:
    cs.endwin()
