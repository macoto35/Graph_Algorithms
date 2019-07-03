def isBipartite(adjList, visited, color, v):
    print('enter isbipartite: ', v)
    for u in adjList[v]:
        print('in for u: ', u)
        if visited[u] == False:
            print('not visited: ', v, u)
            visited[u] = True
            color[u] = not color[v]
            if not isBipartite(adjList, visited, color, u):
                print('return zero: ', v, u)
                return 0
        elif color[v] == color[u]:
            print('visited and same color: ', v, u)
            return 0
    
    print('end of for: ', v, u)
    return 1

n, m = map(int, input().split())
adjList = [[] for i in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    adjList[u].append(v)
    adjList[v].append(u)

visited = [False for i in range(n+1)]
color = [-1 for i in range(n+1)]
visited[1] = True
color[1] = 0
print(isBipartite(adjList, visited, color, 1))
