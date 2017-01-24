import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

N = int(input()) # the number of temperatures to analyse
TEMPS = input() # the N temperatures expressed as integers ranging from -273 to 5526

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
TEMPS = list(map(int, TEMPS.split()))

def abs(n):
    return (n,-n)[n<0]

res = 0
tmp = 5527

for value in TEMPS:
    if (abs(value) < tmp) or (abs(value) == tmp and value > 0):
        res = value
        tmp = abs(value)


print(res)