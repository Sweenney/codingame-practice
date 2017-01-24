import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

alpha = "abcdefghijklmnopqrstuvwxyz?"
asciiChar = dict()

for char in alpha:
    asciiChar[char] = list()

L = int(input())
H = int(input())
T = input()

for i in range(H):
    ROW = input()
    y = 0
    for char in alpha:
        start = y * L
        end = start + L
        asciiChar[char].append(ROW[start:end])
        y += 1

out = list()

for i in range(H):
    out.append("")

for char in T:
    for i in range(H):
        if asciiChar.get(char.lower()):
            out[i] += asciiChar[char.lower()][i]
        else:
            out[i] += asciiChar['?'][i]

for i in range(H):
    print(out[i])
