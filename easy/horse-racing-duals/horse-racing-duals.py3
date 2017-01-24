import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

N = int(input())
Pi = list()

for i in range(N):
    Pi.append(int(input()))

print(Pi, file=sys.stderr)

tmp = max(Pi)
Pi.sort()

print(Pi, file=sys.stderr)

for i in range(len(Pi) - 1):
    if (Pi[i + 1] - Pi[i]) < tmp:
        tmp = (Pi[i + 1] - Pi[i])

print(tmp)