import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

r = int(input())
l = int(input())

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

res = [r]

for i in range(1, l):
    tmp = []

    p = res[0]
    num = res[1:]
    num.append(" ")
    count = 1


    for v in num:
        if v != p:
            tmp.append(count)
            tmp.append(p)
            count = 1
            p = v
        else:
            count += 1

    print("tmp => %s" % tmp, file=sys.stderr)
    res = tmp



print("res : %s" % (res) , file=sys.stderr)


print(*res)
