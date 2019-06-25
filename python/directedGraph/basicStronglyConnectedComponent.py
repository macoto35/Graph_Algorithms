class BasicStronglyConnectedComponent:
    '''basic algorithm - find sink'''
    def basicScc(self, adjList):
        scc = [0 for i in range(len(adjList))]
        group = 1

        while len(adjList) != 0:
            #print('scc: ', scc)
            #print('adjList: ', adjList)
            v = self._dfs(self._reverse(adjList), scc)
            
            if v == -1:
                break

            #print('max v: ', v)
            self.findGroupAndRemoveFromGraph(adjList, scc, v, group)
            group += 1

        return scc

    def _reverse(self, adjList):
        tmp = [[] for i in range(len(adjList))]

        for i in range(len(adjList)):
            for j in adjList[i]:
                tmp[j].append(i)

        return tmp

    def _dfs(self, adjList, scc):
        numOfVertex = len(adjList)
        prepost = [[-1, -1] for i in range(numOfVertex)]
        self.prepostIdx = 1

        for v in range(numOfVertex):
            if prepost[v][0] == -1 and scc[v] == 0:
                self._explore(adjList, prepost, v)

        #print('reverse adjList: ', adjList)
        #print('pre/post: ', prepost)
        idx = val = -1
        for i in range(len(prepost)):
            if prepost[i][1] > val:
                idx = i
                val = prepost[i][1]

        return idx

    def _explore(self, adjList, prepost, v):
        self._pre(prepost, v)

        for u in adjList[v]:
            if prepost[u][0] == -1:
                self._explore(adjList, prepost, u)

        self._post(prepost, v)

    def _pre(self, prepost, v):
        prepost[v][0] = self.prepostIdx
        self.prepostIdx += 1

    def _post(self, prepost, v):
        prepost[v][1] = self.prepostIdx
        self.prepostIdx += 1

    def findGroupAndRemoveFromGraph(self, adjList, scc, v, group):
        scc[v] = group

        for u in adjList[v]:
            if scc[u] == 0:
                self.findGroupAndRemoveFromGraph(adjList, scc, u, group)

        for i in range(len(adjList)):
            try:
                adjList[i].remove(v)
            except:
                continue
