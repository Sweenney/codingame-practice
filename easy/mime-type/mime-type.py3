import sys, math
import os.path

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

N = int(input()) # Number of elements which make up the association table.
Q = int(input()) # Number Q of file names to be analyzed.

ext = dict()
for i in range(N):
    # EXT: file extension
    # MT: MIME type.
    EXT, MT = input().split()
    ext[EXT.lower()] = MT

print(ext, file=sys.stderr)

for i in range(Q):
    FNAME = input() # One file name per line.
    unknown = False
    #print(FNAME, file=sys.stderr)
    key = FNAME.rsplit('.', 1) #FNAME.rsplit('.', 1)     #.lower()
    print("Filename " + FNAME + ", ext found : " + str(key), file=sys.stderr)
    if len(key) > 1:
        key = key[-1:][0].lower()
        if ext.get(key):
            print(ext.get(key))
        else:
            unknown = True
    else:
        unknown = True

    if unknown == True:
        print("UNKNOWN")



# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)