import math


def get_factors(x):
    flist = []
    factor = 2
    sq = math.sqrt(x) + 1
    while factor < sq:
        if x % factor ==0:
            flist.append(factor)
            x = x/factor
        else:
            factor += 1
    if flist == []:
        return [x]
    return flist


def count_power(flist):
    diction = {}
    for i in flist:
        if i in diction.keys():
            diction[i] += 1
        else:
            diction[i] = 1
    return min(diction.values())


x = int(input())
while x != 0:
    print(count_power(get_factors(x)))
    x = int(input())
