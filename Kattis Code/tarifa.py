data = int(input())
months = int(input())
sum = 0
for i in range(months):
    sum += int(input())
print((months+1)*data-sum)