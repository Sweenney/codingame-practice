import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# lightX: the X position of the light of power
# lightY: the Y position of the light of power
# initialTX: Thor's starting X position
# initialTY: Thor's starting Y position
lightX, lightY, initialTX, initialTY = [int(i) for i in input().split()]


thorX = initialTX
thorY = initialTY
# game loop
while 1:

    directionX = ""
    directionY = ""
    if thorX > lightX:
        directionX = "W"
        thorX -= 1
    elif thorX < lightX:
        directionX = "E"
        thorX += 1
    if thorY > lightY:
        directionY = "N"
        thorY -= 1
    elif thorY < lightY:
        directionY = "S"
        thorY += 1
    print(directionY+directionX)