
def minCostFlight(graph, n, origin, dest):
    cost = [float('inf') for i in range(n+1)]
    prev = [None for i in range(n+1)]
    cost[origin] = 0

    pq, idx = createPriorityQueue(n, origin)
    #print(pq, idx)

    while len(pq) != 0:
        u = extractMin(pq, idx)

        if u[0] != float('inf'):
            for v, w in graph[u[0]]:
                if cost[v] > cost[u[0]] + w:
                    cost[v] = cost[u[0]] + w
                    prev[v] = u[0]
                    changePriority(pq, idx, cost, v)
    
    return -1 if cost[dest] == float('inf') else cost[dest]

def createPriorityQueue(n, origin):
    pq = [[i, float('inf')] for i in range(n+1)]
    idx = [i for i in range(n+1)]

    pq[1] = [origin, 0]
    idx[1] = origin

    pq[origin][0] = 1
    idx[origin] = 1

    return pq, idx

def extractMin(pq, idx):
    size = len(pq)
    
    if size == 1:
        result = pq[0]
        pq.pop()
        return result
    
    result = pq[1]
    pq[1] = pq[size - 1]
    idx[result[0]] = None
    idx[pq[1][0]] = 1
    pq.pop()

    shiftDown(1, pq, idx)

    return result

def changePriority(pq, idx, cost, v):
    i = idx[v]
    oldp = pq[i][1]
    newp = pq[i][1] = cost[v]

    if newp < oldp:
        shiftUp(i, pq, idx)
    else:
        shiftDown()

def shiftDown(i, pq, idx):
    minIdx = i
    size = len(pq)

    l = leftChild(i)
    if l < size and pq[l] < pq[minIdx]:
        minIdx = l

    r = rightChild(i)
    if r < size and pq[r] < pq[minIdx]:
        minIdx = r

    if minIdx != i:
        idx[pq[minIdx][0]], idx[pq[i][0]] = idx[pq[i][0]], idx[pq[minIdx][0]]
        pq[minIdx], pq[i] = pq[i], pq[minIdx]
        shiftDown(minIdx, pq, idx)

def shiftUp(i, pq, idx):
    while i > 1 and pq[i][1] < pq[parent(i)][1]:
        p = parent(i)
        idx[pq[i][0]], idx[pq[p][0]] = idx[pq[p][0]], idx[pq[i][0]]
        pq[i], pq[p] = pq[p], pq[i]
        i = p

def leftChild(i):
    return i*2

def rightChild(i):
    return i*2+1

def parent(i):
    return i//2



n, m = map(int, input().split()) #n: num of vertices, m: num of edges
graph = [[] for i in range(n+1)]
for i in range(m):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])
origin, dest = map(int, input().split())

print(minCostFlight(graph, n, origin, dest))
