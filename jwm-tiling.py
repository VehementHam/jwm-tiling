#!/usr/bin/env python
import sys
import subprocess as sp


SCREEN_RESOLUTION = [int(value) for value in (sp
    .check_output(["xrandr | grep '*' | tr -s ' ' | cut -d ' ' -f 2"],
                  shell=True)
    .decode("UTF-8")
    .strip()
    .split("x")
)]

BAR_HEIGHT = 21

GAP_SIZE = 4


ACTIVE_WINDOW = sp.check_output(["xdotool", "getactivewindow"]).decode("UTF-8")


def tile_left():
    sp.run(["xdotool", "windowmove", ACTIVE_WINDOW, "5", "43"])
    sp.run(["xdotool", "windowsize", ACTIVE_WINDOW, "983", "700"])


def tile_right():
    sp.run(["xdotool", "windowmove", ACTIVE_WINDOW, "500", "43"])
    sp.run(["xdotool", "windowsize", ACTIVE_WINDOW, "983", "700"])


try:
    if sys.argv[1] == "left":
        tile_left()
    elif sys.argv[1] == "right":
        tile_right()

except IndexError:
    print(SCREEN_RESOLUTION)
    # print('Please, provide "left" or "right" as an argument')
