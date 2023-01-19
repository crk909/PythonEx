houses,num = [int(i) for i in input().split()]

# Initialize dictionary of associations
# Each house has a list of connected houses and an attribute, turned to true when visited
net_dict = {}
for i in range(1,houses+1):                 # Time complexity of n
    net_dict[i] = []

# Add directly connected houses to the dictionary
for j in range(num):                        # Time complexity of k
    a,b = [int(i) for i in input().split()]
    net_dict[a].append(b)
    net_dict[b].append(a)

# Make bit array disconnected
disconnected = [1] * (houses + 1)


# BFS on tree to update all connected nodes
to_visit = [1]
disconnected[1] = 0
while len(to_visit) != 0:                   # Time complexity of n
    visiting = to_visit.pop(0)
    for neighbour in net_dict[visiting]:    # Time complexity of K
        if disconnected[neighbour]:
            to_visit.append(neighbour)
            disconnected[neighbour] = 0

                                            # Independent, so n + k


# Now just loop through dictionary finding the objects not connected
to_print = True
for i in range(1,houses+1):                 # n
    if disconnected[i]:
        print(i)
        to_print = False

if to_print:
    print("Connected")

# Too slow
# Change implementation of visited
# Just make single list within dictionary
# Don't make a second thing in it for False or True

# Instead make disconnected immediately as bit array
# Update index to 0 when visited
# At end just print each index where still 1
# If all 0 print "Connected"