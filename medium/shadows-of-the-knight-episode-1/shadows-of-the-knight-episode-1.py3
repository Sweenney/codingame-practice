import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# W: width of the building.
# H: height of the building.
W, H = [int(i) for i in input().split()]
N = int(input()) # maximum number of turns before game over.
X0, Y0 = [int(i) for i in input().split()]

HMin = 0
HMax = H
WMin = 0
WMax = W

# game loop
while 1:
    BOMB_DIR = input() # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    X = X0
    Y = Y0

    if "U" in BOMB_DIR:
        HMax = Y - 1
        Y = Y + (HMin - Y - 1) // 2
    elif "D" in BOMB_DIR:
        HMin = Y + 1
        Y = Y + (HMax - Y + 1) // 2
    if "L" in BOMB_DIR:
        WMax = X0 - 1
        X = X + (WMin - X - 1) // 2
    elif "R" in BOMB_DIR:
        WMin = X0 + 1
        X = X + (WMax - X + 1) // 2

    X0 = X
    Y0 = Y

    print(str(X) + " " + str(Y)) # the location of the next window Batman should jump to.