class FindingSink:
    def __init__(self):
        pass

    def linearOrder(self, adjList):
        result = []
        numOfVertex = len(adjList)

        while True:
            # follow a path until cannot extend. find sink v.
            v = 0
            while len(adjList[v]) != 0:
                v = adjList[v][0]

            # put sink v to result
            result.insert(0, v)
            
            if v == 0:
                break

            # remove sink v from G
            for arr in adjList:
                try:
                    arr.remove(v)
                except ValueError:
                    continue
        
        return result

    def topologicalSort(self, adjList):
        return self._dfs(adjList)

    def _dfs(self, adjList):
        visited = [False for i in range(len(adjList))]
        result = []

        for v in range(len(adjList)):
            if visited[v] == False:
                self._explore(adjList, visited, result, v)

        return result

    def _explore(self, adjList, visited, result, v):
        visited[v] = True

        for u in adjList[v]:
            if visited[u] == False:
                self._explore(adjList, visited, result, u)

        result.insert(0, v)
