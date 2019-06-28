def findCycle(adjList, n):
    for v in range(1, n+1):
        visited = [0 for i in range(n+1)]
        explore(adjList, visited, v)

        if visited[v] == 2:
            return 1
    return 0

def explore(adjList, visited, v):
    visited[v] += 1

    for u in adjList[v]:
        if visited[u] == 0:
            explore(adjList, visited, u)
        else:
            visited[u] += 1

n, m = map(int, input().split())
adjList = [[] for i in range(n + 1)]
for i in range(m):
    u, v = map(int, input().split())
    adjList[u].append(v)

print(findCycle(adjList, n))
