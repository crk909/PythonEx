numOwners, teamSize = [int(x) for x in input().split()]

preferences = []
selections = []
for i in range(numOwners):
    selections.append([])
    preProcessing = input().split()
    if (len(preProcessing) == 1):
        preferences.append(list())
    else:
        preferences.append(preProcessing[1:])

playerCount = int(input())
previousRankings = list()
availability = {}
for j in range(playerCount):
    readPlayer = input()
    previousRankings.append(readPlayer)
    availability[readPlayer] = True

# print(selections)
# print(preferences)
# print(previousRankings)

def makeSelection(preferenceList, selectedList):
    selectionMade = False
    while(not selectionMade):
        if (len(preferenceList) == 0):
            trypick = previousRankings.pop(0)
            if(availability[trypick]):
                availability[trypick] = False
                selectedList.append(trypick)
                selectionMade = True
        else:
            trypick = preferenceList.pop(0)
            if(availability[trypick]):
                availability[trypick] = False
                selectedList.append(trypick)
                selectionMade = True

for round in range(teamSize):
    for owner in range(numOwners):
        makeSelection(preferences[owner],selections[owner])


for team in selections:
    print(" ".join(team))


    