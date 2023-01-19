max_guess = 1000
min_guess = 1
not_done = True

while not_done:
    mid = int((max_guess+min_guess+1)/2)
    print(mid, flush=True)
    ans = input()
    if ans == "lower":
        max_guess = mid - 1
    elif ans == "higher":
        min_guess = mid + 1
    else:
        not_done = False
