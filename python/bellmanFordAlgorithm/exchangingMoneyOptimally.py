
def relax(cost, u, v, w, mc):
    if cost[v] > cost[u] + w:
        cost[v] = cost[u] + w
        if mc != None:
            mc[v] = 1

def bellmanFord(graph, n, origin):
    cost = [float('inf') for i in range(n+1)]
    cost[origin] = 0

    for i in range(n-1):
        for u, v, w in graph:
            relax(cost, u, v, w, None)

    #print('-----before->', cost)
    minusCycle = [0 for i in range(n+1)]
    for u, v, w in graph:
        relax(cost, u, v, w, minusCycle)
    #print('-----after->', cost, minusCycle)

    for i in range(1, n+1):
        if cost[i] == float('inf'):
            print('*')
        elif minusCycle[i] == 1:
            print('-')
        else:
            print(cost[i])

n, m = map(int, input().split()) # n: vertices, m: edges
graph = []
for i in range(m):
    graph.append([*map(int, input().split())])
origin = int(input())

bellmanFord(graph, n, origin)

