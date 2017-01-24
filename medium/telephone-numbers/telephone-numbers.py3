import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

count = 0

class Number:
    def __init__(self, value):
        #print("create number (" + str(value) + ")", file=sys.stderr)
        self.value = value
        self.next = dict()

N = int(input())
num = dict()

count = 0

for i in range(N):
    telephone = input()
    next = num
    for c in telephone:
        if not c in next.keys():
           # print(str(c) + " not found", file=sys.stderr)
            next[c] = Number(c)
            count += 1
        next = next[c].next
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)




# The number of elements (referencing a number) stored in the structure.
print(count)
