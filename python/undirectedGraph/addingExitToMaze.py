# compute the number of connected components
def addingExitToMaze(adjList, numOfNodes):
    visited = [False for i in range(numOfNodes+1)]
    group = 0

    for v in range(1, numOfNodes+1):
        if visited[v] == False:
            explore(adjList, visited, v)
            group += 1
    
    return group

def explore(adjList, visited, v):
    visited[v] = True
    
    for u in adjList[v]:
        if visited[u] == False:
            explore(adjList, visited, u)

n, m = map(int, input().split())
adjList = [[] for i in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    adjList[u].append(v)
    adjList[v].append(u)

print('result: ', addingExitToMaze(adjList, n))

