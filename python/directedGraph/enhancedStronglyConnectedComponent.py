from operator import itemgetter

class EnhancedStronglyConnectedComponent:
    def enhancedScc(self, adjList):
        prepost = sorted(self._dfs(self._reverse(adjList)), key=itemgetter(1), reverse=True)
        scc = [0 for i in range(len(adjList))]
        group = 1

        for pre, post, v in prepost:
            if scc[v] == 0:
                self._find(adjList, scc, group, v)
                group += 1

        return scc

    def _reverse(self, adjList):
        tmp = [[] for i in range(len(adjList))]

        for i in range(len(adjList)):
            for j in adjList[i]:
                tmp[j].append(i)
        return tmp

    def _dfs(self, adjList):
        prepost = [[-1, -1, i] for i in range(len(adjList))]
        self.prepostIdx = 1

        for v in range(len(adjList)):
            if prepost[v][0] == -1:
                self._explore(adjList, prepost, v)

        return prepost

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

    def _find(self, adjList, scc, group, v):
        scc[v] = group

        for u in adjList[v]:
            if scc[u] == 0:
                self._find(adjList, scc, group, u)

