def determineOrderCourse(adjList, n):
    visited = [0 for i in range(n+1)]
    stack = []

    for v in range(1, n+1):
        if visited[v] == 0:
            explore(adjList, visited, stack, v)

    for i in range(len(stack)-1, -1, -1):
        print(stack[i], end=' ')

def explore(adjList, visited, stack, v):
    visited[v] = 1

    for u in adjList[v]:
        if visited[u] == 0:
            explore(adjList, visited, stack, u)

    stack.append(v)

n, m = map(int, input().split())
adjList = [[] for i in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    adjList[u].append(v)

determineOrderCourse(adjList, n)
