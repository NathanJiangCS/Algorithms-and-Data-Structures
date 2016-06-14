#Python implementation of shortest path faster algorithm
#Implementation for weighted graphs. Graphs can have negative values

infinity = float('inf')

#a is the adjacency list representation of the matrix
#start is the initial node, end is the destination node
def spfa(a, start, end):
    n = len(a)
    distances = [infinity for i in range(n)]
    distances[start] = 0
    q = [start]

    while len(q):
        currentNode = q.pop(0)
        for i in a[currentNode]:
            nextNode, distance = i
            if distances[nextNode] > distances[currentNode] + distance:
                distances[nextNode] = distances[currentNode] + distance
                q.append(nextNode)

    return distances, distances[end]

