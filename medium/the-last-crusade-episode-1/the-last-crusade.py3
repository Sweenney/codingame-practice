# vim: ft=python
# -*- python -*-

import sys, math
import shlex

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# W: number of columns.
# H: number of rows.
W, H = [int(i) for i in input().split()]
map = []
for i in range(H):
    LINE = input() # represents a line in the grid and contains W integers. Each integer represents one room of a given type.
    map.append(shlex.split(LINE))
EX = int(input()) # the coordinate along the X axis of the exit (not useful for this first mission, but must be read).

pieces = dict()
pieces["0"] = {"RIGHT": False, "LEFT": False, "TOP": False}
pieces["1"] = {"RIGHT": "DOWN", "LEFT": "DOWN", "TOP": "DOWN"}
pieces["2"] = {"RIGHT": "LEFT", "LEFT": "RIGHT", "TOP": False}
pieces["3"] = {"RIGHT": False, "LEFT": False, "TOP": "DOWN"}
pieces["4"] = {"RIGHT": "DOWN", "LEFT": False, "TOP": "LEFT"}
pieces["5"] = {"RIGHT": False, "LEFT": "DOWN", "TOP": "RIGHT"}
pieces["6"] = {"RIGHT": "LEFT", "LEFT": "RIGHT", "TOP": False}
pieces["7"] = {"RIGHT": "DOWN", "LEFT": False, "TOP": "DOWN"}
pieces["8"] = {"RIGHT": "DOWN", "LEFT": "DOWN", "TOP": False}
pieces["9"] = {"RIGHT": False, "LEFT": "DOWN", "TOP": "DOWN"}
pieces["10"] = {"RIGHT": False, "LEFT": False, "TOP": "LEFT"}
pieces["11"] = {"RIGHT": False, "LEFT": False, "TOP": "RIGHT"}
pieces["12"] = {"RIGHT": "DOWN", "LEFT": False, "TOP": False}
pieces["13"] = {"RIGHT": False, "LEFT": "DOWN", "TOP": False}

def next(X,Y,pos,type):

    dir = pieces[type][pos]
    
    if dir == "DOWN":
        Y +=1
    elif dir == "RIGHT":
        X +=1
    elif dir == "LEFT":
        X -= 1
    return (X,Y)

# game loop
while 1:
    XI, YI, POS = input().split()
    XI = int(XI)
    YI = int(YI)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    print("%s %s" % next(XI, YI, POS, map[YI][XI]))
