x = int(input())
for i in range(x):
    s = input()
    s_length = len(s)
    count = 1
    while count < s_length:
        new_string = s[0:count] * int((s_length/count)+1)
        if(s in new_string):
            break
        count += 1
    print(count)
