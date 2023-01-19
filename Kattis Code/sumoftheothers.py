import sys

while True:
    next_line = sys.stdin.readline()
    if(next_line == ''):
        break
    else:
        new_list = [int(x) for x in next_line.split()]
        cool = sum(new_list)
        print(int(cool/2))


