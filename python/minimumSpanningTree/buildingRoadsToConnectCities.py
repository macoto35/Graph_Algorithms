from math import sqrt

def findMinTotalLenOfSegment(n, coordinates, maxX, maxY):
    graph = getGraph(coordinates)
    #print(graph)

    parent, rank = createPrioritySet(maxX, maxY)
    #print(parent, rank)

    result = 0
    for u, v, w in graph:
        if find(u, parent, rank) != find(v, parent, rank):
            union(u, v, parent, rank)
            result += w
    
    return result

# coordinates to graph sorted by ASC
def getGraph(coordinates):
    graph = []
    
    for i in range(len(coordinates)):
        for j in range(i+1, len(coordinates)):
            x = coordinates[i];
            y = coordinates[j];
            graph.append([x, y, sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)])

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

# priority set
def createPrioritySet(maxX, maxY):
    parent = [[[i, j] for j in range(maxY)] for i in range(maxX)]
    rank = [[0 for j in range(maxY)] for i in range(maxX)]
    
    return parent, rank

def find(i, parent, rank):
    while i != parent[i[0]][i[1]]:
        i = parent[i[0]][i[1]]

    return i

def union(i, j, parent, rank):
    i_id = find(i, parent, rank)
    j_id = find(j, parent, rank)

    if i_id == j_id:
        return

    if rank[i_id[0]][i_id[1]] > rank[j_id[0]][j_id[1]]:
        parent[j_id[0]][j_id[1]] = i_id
    else:
        parent[i_id[0]][i_id[1]] = j_id
        if rank[i_id[0]][i_id[1]] == rank[j_id[0]][j_id[1]]:
            rank[j_id[0]][j_id[1]] += 1


n = int(input())
coordinates = []
maxX, maxY = 0, 0
for i in range(n):
    x, y = map(int, input().split())
    coordinates.append([x, y])
    if x > maxX:
        maxX = x
    if y > maxY:
        maxY = y

print(findMinTotalLenOfSegment(n, coordinates, maxX+1, maxY+1))

