from random import randint

def checkingIntersectionReachable(adjList, n):
    revAdjList = reverseGraph(adjList, n)
    visited = initVisited(n)
    post = [[0, i+1] for i in range(n)]

    for v in range(1, n+1):
        if visited[v] == 0:
            explore(revAdjList, visited, post, v)

    quickSort(post, 0, len(post) - 1)
    visited = initVisited(n)
    group = 0
    for i, v in post:
        if visited[v] == 0:
            explore(adjList, visited, None, v)
            group += 1

    print("# of SCC: ", group)

def initVisited(n):
    return [0 for i in range(n+1)]

def explore(adjList, visited, post, v):
    visited[v] = 1

    for u in adjList[v]:
        if visited[u] == 0:
            explore(adjList, visited, post, u)
    
    if post is not None:
        setPostNum(post, v)

def setPostNum(post, v):
    global idx
    post[v-1][0] = idx
    idx += 1

def reverseGraph(adjList, n):
    revAdjList = [[] for i in range(n+1)]
    for i in range(1, n+1):
        for j in adjList[i]:
            revAdjList[j].append(i)
    return revAdjList

def quickSort(arr, st, ed):
    if st >= ed:
        return
    
    i = st
    j = ed
    pivot= randint(st, ed)

    while i < j:
        while i < ed and arr[i] > arr[pivot]:
            i += 1
        while j > st and arr[j] < arr[pivot]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]

    quickSort(arr, st, pivot-1)
    quickSort(arr, pivot+1, ed)

idx = 1
n, m = map(int, input().split())
adjList = [[] for i in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    adjList[u].append(v)

checkingIntersectionReachable(adjList, n)
