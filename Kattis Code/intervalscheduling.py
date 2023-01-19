x = int(input())
y = []
count = 0

for i in range(x):
    y.append([int(i) for i in input().split()])

sorted_y = sorted(y, key=lambda interval: interval[1])

time_cut = 0
while len(sorted_y) != 0:
    if sorted_y[0][0] >= time_cut:
        time_cut = sorted_y[0][1]
        count += 1
    else:
        sorted_y.pop(0)

print(count)
