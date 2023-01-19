import math

x = int(input())
while x != 0:
    flist = []
    factor = 2
    sq = int(math.sqrt(x) + 1)
    while factor < sq:
        if x % factor == 0:
            flist.append(factor)
            x = x/factor
        else:
            factor += 1
    if flist == []:
        flist.append(x)
    diction = {}
    for i in flist:
        if i in diction.keys():
            diction[i] += 1
        else:
            diction[i] = 1
    print(min(diction.values()))
    x = int(input())
