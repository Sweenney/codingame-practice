import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

MESSAGE = input()

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

array = ''.join(format(ord(x), '07b') for x in MESSAGE)

lastByte = '3'
tmp = ''
i = 0

#print(array, file=sys.stderr)

for byte in array:
    #print(byte, file=sys.stderr)
    if byte == ' ':
        print(" ", end="")
    elif byte == '1':
        if lastByte == byte:
            tmp += "0"
        else:
            print(tmp + (' ' * i), end="")
            tmp = "0 0"
            lastByte = byte
    elif byte == '0':
        if lastByte == byte:
            tmp += "0"
        else:
            print(tmp + (' ' * i), end="")
            tmp = "00 0"
            lastByte = byte
    if i == 0:
        i += 1

print(tmp, end="")

#0100101