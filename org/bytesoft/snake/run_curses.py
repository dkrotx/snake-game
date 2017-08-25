#!/usr/bin/python3
import curses
from curses_ui import CursesDrawer
from engine import Engine


def main(scr):
    curses.curs_set(False)
    engine = Engine(CursesDrawer(scr), 8, 8)
    engine.start()

    while not engine.is_finished():
        c = scr.getch()

        if c == curses.KEY_LEFT:
            engine.turn_left()
        elif c == curses.KEY_RIGHT:
            engine.turn_right()
        elif c == curses.KEY_UP:
            engine.turn_up()
        elif c == curses.KEY_DOWN:
            engine.turn_down()
        elif c == curses.KEY_F10:
            engine.quit()
            break

    engine.join()


curses.wrapper(main)
