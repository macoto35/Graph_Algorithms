
def relax(cost, u, v, w):
    if cost[v] > cost[u] + w:
        cost[v] = cost[u] + w

def detectNegativeCycle(graph, n):
    '''
    # check all nodes
    for origin in range(1, n+1):
        cost = [float('inf') for i in range(n+1)]
        cost[origin] = 0

        for i in range(n-1):
            for u, v, w in graph:
                relax(cost, u, v, w)

        for u, v, w in graph:
            if cost[v] > cost[u] + w:
                return 1
    return 0
    '''

    # check only minus weight edges
    for origin, j, k in graph:
        if k < 0:
            cost = [float('inf') for i in range(n+1)]
            cost[origin] = 0

            for i in range(n-1):
                for u, v, w in graph:
                    relax(cost, u, v, w)

            for u, v, w in graph:
                if cost[v] > cost[u] + w:
                    return 1
    return 0

n, m = map(int, input().split()) #n: num of vertex, m: num of edge
graph = []
for i in range(m):
    graph.append([*map(int, input().split())])

print(detectNegativeCycle(graph, n))

