import sys

dict = {
    'A': ".-",
    'B': "-...",
    'C': "-.-.",
    'D': "-..",
    'E': ".",
    'F': "..-.",
    'G': "--.",
    'H': "....",
    'I': "..",
    'J': ".---",
    'K': "-.-",
    'L': ".-..",
    'M': "--",
    'N': "-.",
    'O': "---",
    'P': ".--.",
    'Q': "--.-",
    'R': ".-.",
    'S': "...",
    'T': "-",
    'U': "..-",
    'V': "...-",
    'W': ".--",
    'X': "-..-",
    'Y': "-.--",
    'Z': "--..",
    '?': "----",
    '.': "---.",
    ',': ".-.-",
    '_': "..--"}

while True:
    next_line = sys.stdin.readline().strip()
    if next_line == '':
        break
    else:
        num_list = []
        morse = ""
        message = ""
        for i in next_line:
            morse += dict[i]
            x = len(dict[i])
            num_list.append(x)
        num_list.reverse()
        idx = 0;
        for j in num_list:
            char = morse[idx:idx+j]
            for k,v in dict.items():
                if char == v:
                    message += k
            idx += j
        print(message)