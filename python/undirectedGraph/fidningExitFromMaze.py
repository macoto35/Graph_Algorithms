def findExit(adjList, visited, source):
	visited[source] = True	
	for v in adjList[source]:
		if visited[v] == False:
			findExit(adjList, visited, v)

n, m = map(int, input().split())
adjList = [[] for i in range(n + 1)]
for i in range(m):
	u, v = map(int, input().split())
	adjList[u].append(v)
	adjList[v].append(u)
source, target = map(int, input().split())

visited = [False for i in range(n+1)]
findExit(adjList, visited, source)
print('result? ', visited[target])
