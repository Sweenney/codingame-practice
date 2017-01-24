import sys, math

# Don't let the machines win. You are humanity's last hope...
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

width = int(input()) # the number of cells on the X axis
height = int(input()) # the number of cells on the Y axis
line = list()
for i in range(height):
    line.append(input()) # width characters, each either 0 or .

print(line, file=sys.stderr)

# print("0 0 1 0 0 1") # Three coordinates: a node, its right neighbor, its bottom neighbor
# print("1 0 -1 -1 -1 -1")
# print("0 1 -1 -1 -1 -1")

def next_in_line(x, y):
    for i in range(x + 1, width):
        if i < width and line[y][i] != ".":
            print(str(i) + " " + str(y) + " ", end="")
            return
    print("-1 -1 ", end="")

def next_in_column(x, y):
    for i in range(y + 1, height):
        if i < height and line[i][x] != ".":
            print(str(x) + " " + str(i) + " ")
            return
    print("-1 -1")

for y in range(height):
    for x in range(width):
        print("coord : [" + str(x) + "][" + str(y) + "]", file=sys.stderr)
        if line[y][x] != ".":
            print(str(x) + " " + str(y) + " ", end="")
            next_in_line(x, y)
            next_in_column(x, y)