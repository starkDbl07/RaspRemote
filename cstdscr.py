'''
Curses stdscr initialization for CXenTerm
'''

import curses as cs
import locale


def start():
    '''
        Start stdscr session with default configurations
        and return the stdscr object.
    '''
    # Set locale to enable unicode support
    locale.setlocale(locale.LC_ALL,"")

    # Initialize stdscr with default behaviour
    stdscr = cs.initscr()
    cs.noecho()                 # disable echoing
    cs.curs_set(0)              # disable cursor visibility
    stdscr.keypad(1)            # enable function keys

    cs.start_color()            # enable colors
    cs.use_default_colors()     # enable transparency
    return stdscr               # return the stdscr object


def end():
    '''
        End stdscr session
    '''
    cs.endwin()             # end stdscr
