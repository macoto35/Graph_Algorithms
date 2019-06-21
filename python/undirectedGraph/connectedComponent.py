class ConnectedComponent:
    def __init__(self, numOfVertex):
        self._init(numOfVertex)
        
    def _init(self, numOfVertex):
        self.visited = [False for i in range(numOfVertex)]
        self.cc = [0 for i in range(numOfVertex)]

    def connectedComponentDFS(self, adjList, numOfVertex):
        self._init(numOfVertex)
        group = 1

        for v in range(numOfVertex):
            if self.visited[v] == False:
                self.explore(adjList, v, group)
                group += 1

    def explore(self, adjList, v, group):
        self.visited[v] = True
        self.cc[v] = group

        for u in adjList[v]:
            if self.visited[u] == False:
                self.explore(adjList, u, group)
    
    def getConnectedComponent(self):
        return self.cc
