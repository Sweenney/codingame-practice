# -*- python -*-

import sys, math

surfaceN = int(input()) # the number of points used to draw the surface of Mars.
for i in range(surfaceN):
    # landX: X coordinate of a surface point. (0 to 6999)
    # landY: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    landX, landY = [int(j) for j in input().split()]

    # game loop
    while 1:
        # hSpeed: the horizontal speed (in m/s), can be negative.
        # vSpeed: the vertical speed (in m/s), can be negative.
        # fuel: the quantity of remaining fuel in liters.
        # rotate: the rotation angle in degrees (-90 to 90).
        # power: the thrust power (0 to 4).
        X, Y, hSpeed, vSpeed, fuel, rotate, power = [int(i) for i in input().split()]

        angle = 0
        power = 0
        
        vSpeed *= -1
        if vSpeed >= 40:
            print(str(vSpeed // 10), file=sys.stderr)
            power = (vSpeed // 1)
            if power > 4:
                power = 4


        print(str(angle) + " " + str(power))
