#!/usr/bin/env python
import sys
import subprocess as sp


def tile_left():
    active_window = sp.check_output(["xdotool", "getactivewindow"]).decode("UTF-8")
    sp.run(["xdotool", "windowmove", active_window, "5", "43"])
    sp.run(["xdotool", "windowsize", active_window, "983", "1005"])


def tile_right():
    active_window = sp.check_output(["xdotool", "getactivewindow"]).decode("UTF-8")
    sp.run(["xdotool", "windowmove", active_window, "963", "43"])
    sp.run(["xdotool", "windowsize", active_window, "983", "1005"])


try:
    if sys.argv[1] == "left":
        tile_left()
    elif sys.argv[1] == "right":
        tile_right()

except IndexError:
    print('Please, provide "left" or "right" as an argument')
