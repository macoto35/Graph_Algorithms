class EasyStronglyConnectedComponent:
    ''' naive algorithm '''
    def easyScc(self, adjList):
        numOfVertex = len(adjList)
        scc = [0 for i in range(numOfVertex)]
        group = 1

        for v in range(numOfVertex):
            if scc[v] == 0:
                # find all the path from v
                self._explore(adjList, scc, group, v)
                #print(v, 'after explore: ', scc)

                # mark all the vertex can return to v
                for u in range(len(scc)):
                    visited = self._initVisited(numOfVertex)
                    if scc[u] == group:
                        self._canReturn(adjList, scc, visited, group, v, u)
                #print(v, 'after can return: ', scc)
            
                group += 1
        return scc
    
    def _initVisited(self, n):
        return [False for i in range(n)]

    def _explore(self, adjList, scc, group, v):
        scc[v] = group

        for u in adjList[v]:
            if scc[u] == 0:
                self._explore(adjList, scc, group, u)

    def _canReturn(self, adjList, scc, visited, group, v, u):
        visited[u] = True

        if v == u:
            scc[u] = group
            return group

        idx = -1
        for i in adjList[u]:
            if scc[i] == group and visited[i] == False:
                idx = i
                break

        if idx == -1:
            scc[u] = 0
            return 0
        else:
            scc[u] = self._canReturn(adjList, scc, visited, group, v, idx)
            return scc[u]
