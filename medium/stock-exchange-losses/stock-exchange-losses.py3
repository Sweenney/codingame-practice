import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

def printd(msg):
    print(msg, file=sys.stderr)

n = int(input())
printd(n)
tab = []
for i in input().split():
    tab.append(int(i))
printd(tab)

res = [0]
vh = None

for va in tab:
    if vh != None and vh > va:
        res.append(va - vh)
    if vh == None or vh < va:
        vh = va

printd(res)

print(min(res))
