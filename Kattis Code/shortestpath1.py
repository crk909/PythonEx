from queue import PriorityQueue

INF = 100000000
while True:
    n,m,q,s = [int(i) for i in input().split()]
    # print("Read input: ", n,m,q,s)
    if n == 0 and m == 0 and q == 0 and s == 0:
        break


    # Create priority Q and adjacency list
    PrioQ = PriorityQueue()
    adjacency = []
    for i in range(n):
        adjacency.append([])


    # Create n nodes
    # Will have an array for whether each node is visited, and another for saving the total cost
    isVisited = [0] * n
    totalCost = [INF] * n

    # Set cost of source to 0
    PrioQ.put((0,s))

    # Get m edges, adding to adjacency list
    for i in range(m):
        outgoingNode, incomingNode,edgeWeight = [int(j) for j in input().split()]
        adjacency[outgoingNode].append([incomingNode, edgeWeight])

    # Run algorithm to get the lowest cost for each (Dijkstras)
    while not PrioQ.empty():
        curCost, curNode = PrioQ.get()

        # Only visit if unvisited
        if isVisited[curNode] == 0 : #Tests if unvisited
            isVisited[curNode] = 1 #Set as visited
            totalCost[curNode] = curCost

            # Check neighbours of curNode
            for edge in adjacency[curNode]:
                checkingNode, edgeCost = edge

                # If neighbour unvisited compare cost to previously found. If better, update
                if isVisited[checkingNode] == 0:
                    updateCost = edgeCost + curCost
                    if updateCost < totalCost[checkingNode]:
                        totalCost[checkingNode] = updateCost
                        PrioQ.put((updateCost, checkingNode))

    # Check each query
    for i in range(q):
        checking = int(input())
        # print("Checking cost for: ", checking)
        if totalCost[checking] == INF:
            print("Impossible")
        else:
            print(totalCost[checking])