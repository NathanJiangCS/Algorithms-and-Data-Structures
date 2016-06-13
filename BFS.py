#Breadth first search implementation with python
#Can be used to find either if there is a possible path between 2 paths as well as solving the single source shortest path problem
#for unweighted graphs.

from queue import Queue

# a is the adjacency list that represents the matrix
# start is the starting node. end is the ending node

def bfs(a, start, end):
	n = len(a) #n is the number of nodes
	
	#Keeping track of distances from starting node. Initializing as all infinity
	distance = [1e999 for i in range(n)]

	#We set the distance of the starting node as 0 and add it to the queue.
	distance[start] = 0
	q = Queue()
	q.put(start)

	while not q.empty(): #While our queue is not empty
		u = q.get()
		for i in a[u]:
			if distance[i] == 1e999:
				distance[i] = distance[u] + 1
				q.put(i)

	return distance[end], distance

testAdjacencyList = [ [1, 6, 8],
		      [0, 4, 6, 9],
		      [4, 6],
		      [4, 5, 8],
		      [1, 2, 3, 5, 9],
		      [3, 4],
		      [0, 1, 2],
		      [8, 9],
		      [0, 3, 7],
		      [1, 4, 7] ]
minDistance, distances = bfs(testAdjacencyList, 0, 4)

print minDistance
print distances
