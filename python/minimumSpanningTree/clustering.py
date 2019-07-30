from math import sqrt

def clustering(n, coordinates, k):
    #print(coordinates)
    parent, rank = createPrioritySet(n)
    #print(parent, rank)

    graph = getGraph(coordinates)
    #print(graph)

    if n == k:
        return graph[2]

    result = False
    for u, v, w in graph:
        #print(u, v, w)
        if find(u, parent) != find(v, parent):
            if result:
                return w
            else:
                union(u, v, parent, rank)
                #print(parent, rank)
                result = checkCluster(parent, k)

def checkCluster(parent, k):
    cnt = 0
    for i in range(len(parent)):
        if i == parent[i]:
            cnt += 1
    return cnt == k

# priority set
def createPrioritySet(n):
    parent = [i for i in range(n)]
    rank = [0 for i in range(n)]

    return parent, rank

def find(i, parent):
    if i != parent[i]:
        i = parent[i]
    return i

def union(i, j, parent, rank):
    i_id = find(i, parent)
    j_id = find(j, parent)

    if i_id == j_id:
        return

    if rank[i_id] > rank[j_id]:
        parent[j_id] = parent[i_id]
    else:
        parent[i_id] = parent[j_id]
        if rank[i_id] == rank[j_id]:
            rank[j_id] += 1

# quick sort
def getGraph(coordinates):
    graph = []
    for i in range(len(coordinates)):
        for j in range(i+1, len(coordinates)):
            x = coordinates[i]
            y = coordinates[j]
            graph.append([i, j, sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)])

    quickSort(graph, 0, len(graph) - 1)

    return graph

def quickSort(graph, st, ed):
    if st < ed:
        m1, m2 = getPartition(graph, st, ed)
        
        quickSort(graph, st, m1 - 1)
        quickSort(graph, m2 + 1, ed)

def getPartition(graph, st, ed):
    pivot = getPivot(graph, st, ed)
    m1 = m2 = st

    for i in range(st+1, ed+1):
        if graph[i][2] <= pivot:
            if graph[i][2] < pivot:
                graph[m1], graph[i] = graph[i], graph[m1]
                m1 += 1
            m2 += 1
            graph[m2], graph[i] = graph[i], graph[m2]

    return m1, m2

def getPivot(graph, st, ed):
    mid = (st + ed) // 2
    graph[st], graph[mid] = graph[mid], graph[st]
    return graph[st][2]



n = int(input())
coordinates = {}
maxX = maxY = 0
for i in range(n):
    x, y = map(int, input().split())
    coordinates[i] = [x, y]
    if x > maxX:
        maxX = x
    if y > maxY:
        maxY = y
k = int(input())

print(clustering(n, coordinates, k))

