lines = int(input())

for i in range(lines):
    cur_string = input().upper()
    letter_list = [0]*26
    for letter in cur_string:
        x = ord(letter)
        if x > 64 and x < 91:
            letter_list[x-65] = 1
    missing = ""
    for idx in range(26):
        if letter_list[idx] == 0:
            missing += chr(97+idx)
    if missing == "":
        print("pangram")
    else:
        print("missing " + missing)