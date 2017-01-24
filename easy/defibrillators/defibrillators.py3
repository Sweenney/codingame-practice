import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

LON = input()
LAT = input()
N = int(input())

defibList = dict()

for i in range(N):
    tmp = input().split(';')
    defDict = dict()
    defDict['id'] = tmp[0]
    defDict['name'] = tmp[1]
    defDict['address'] = tmp[2]
    defDict['num'] = tmp[3]
    defDict['lon'] = float(tmp[4].replace(",", "."))
    defDict['lat'] = float(tmp[5].replace(",", "."))
    defibList[int(tmp[0])] = defDict

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

LON = float(LON.replace(",", "."))
LAT = float(LAT.replace(",", "."))

res = None
tmp = None

for key, defib in defibList.items():
    x = (defib['lon'] - LON) * math.cos((LAT + defib['lat']) / 2.0)
    y = (defib['lat'] - LAT)
    d = math.sqrt((x * x) + (y * y)) * 6371
    if tmp and tmp > d:
        res = defib
        tmp = d
    elif not tmp and not res:
        res = defib
        tmp = d

    print(str(key) + ": " + str(d) , file=sys.stderr)

print(res, file=sys.stderr)
print(res['name'])
