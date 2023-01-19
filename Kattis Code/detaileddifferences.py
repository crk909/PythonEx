x = int(input())
for i in range(x):
    str1 = input()
    str2 = input()
    output = ""
    for c in range(len(str1)):
        if str1[c] == str2[c]:
            output += "."
        else:
            output += "*"
    print(str1)
    print(str2)
    print(output)

