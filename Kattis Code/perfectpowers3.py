import math


def get_factors(x):
    dict = {}
    factor = 2
    sq = int(math.sqrt(x)) + 1
    while factor < sq:
        if x % factor == 0:
            if factor in dict:
                dict[factor] += 1
            else:
                dict[factor] = 1
            x = x/factor
        else:
            factor += 1
    if len(dict.keys()) == 0:
        return 1
    return max(min(dict.values()), 1)


x = int(input())
while(x != 0):
    print(get_factors(x))
    x = int(input())
