class DepthFirstSearch:
    def __init__(self, numOfVertex):
        self.initVisited(numOfVertex)

    def getVisited(self):
        return self.visited

    def initVisited(self, numOfVertex):
        self.visited = [False for i in range(numOfVertex)]
    
    def explore(self, adjList, v):
        self.visited[v] = True

        for u in adjList[v]:
            if self.visited[u] == False:
                self.explore(adjList, u)

    def depthFirstSearch(self, adjList, numOfVertex):
        self.initVisited(numOfVertex)

        for v in range(numOfVertex):
            if self.visited[v] == False:
                self.explore(adjList, v)
