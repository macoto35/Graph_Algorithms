def bfs(adjList, numOfVertex, origin, dest):
    dist = [-1 for i in range(numOfVertex+1)]
    dist[origin] = 0
    queue = [origin]

    while len(queue) != 0:
        u = queue.pop(0)
        for v in adjList[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                queue.append(v)

    return dist[dest]

n, m = map(int, input().split())
adjList = [[] for i in range(n+1)]
for i in range(m):
    v1, v2 = map(int, input().split())
    adjList[v1].append(v2)
    adjList[v2].append(v1)
u, v = map(int, input().split())

print(bfs(adjList, n, u, v))
