import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# nbFloors: number of floors
# width: width of the area
# nbRounds: maximum number of rounds
# exitFloor: floor on which the exit is found
# exitPos: position of the exit on its floor
# nbTotalClones: number of generated clones
# nbAdditionalElevators: ignore (always zero)
# nbElevators: number of elevators
nbFloors, width, nbRounds, exitFloor, exitPos, nbTotalClones, nbAdditionalElevators, nbElevators = [int(i) for i in input().split()]

elev = dict()
elev[exitFloor] = exitPos
for i in range(nbElevators):
    # elevatorFloor: floor on which this elevator is found
    # elevatorPos: position of the elevator on its floor
    elevatorFloor, elevatorPos = [int(j) for j in input().split()]
    elev[elevatorFloor] = elevatorPos

# game loop
while 1:
    # cloneFloor: floor of the leading clone
    # clonePos: position of the leading clone on its floor
    # direction: direction of the leading clone: LEFT or RIGHT
    cloneFloor, clonePos, direction = input().split()
    cloneFloor = int(cloneFloor)
    clonePos = int(clonePos)

    if clonePos >= width - 1 or clonePos <= 0:
        print("BLOCK")
    elif cloneFloor in elev and clonePos > elev[cloneFloor] and direction == "RIGHT":
        print("BLOCK")
    elif cloneFloor in elev and clonePos < elev[cloneFloor] and direction == "LEFT":
        print("BLOCK")
    else:
        print("WAIT")