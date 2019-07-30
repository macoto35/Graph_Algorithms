class PrimAlgorithm:
    def run(self, graph, numOfVertex):
        cost = [float('inf') for i in range(numOfVertex)]
        parent = [None for i in range(numOfVertex)]

        cost[0] = 0
        pq, idx = self._createPriorityQueue(numOfVertex)

        while len(pq) > 0:
            v = self._extractMin(pq, idx)

            for u,w in graph[v]:
                if idx[u] != None and cost[u] > w:
                    cost[u] = w
                    parent[u] = v
                    self._changePriority(u, pq, idx, cost)
                    #print(v, u, w, cost, parent, pq, idx)
        
        return [cost, parent]

    def _createPriorityQueue(self, n):
        pq = [[i, float('inf')] for i in range(n)]
        pq[0][1] = 0
        idx = [i for i in range(n)]

        return pq, idx

    def _extractMin(self, pq, idx):
        result = pq[0]

        if len(pq) == 1:
            pq.pop()
            idx[result[0]] = None
            return result[0]

        pq[0] = pq[len(pq) - 1]
        pq.pop()
        idx[pq[0][0]] = 0
        idx[result[0]] = None

        self._shiftDown(0, pq, idx)

        return result[0]

    def _changePriority(self, i, pq, idx, cost):
        key = idx[i]

        oldp = pq[key][1]
        newp = pq[key][1] = cost[i]

        if newp < oldp:
            self._shiftUp(key, pq, idx)
        else:
            self._shiftDown(key, pq, idx)

    def _shiftUp(self, i, pq, idx):
        while i > 0 and pq[i][1] < pq[self._parent(i)][1]:
            p = self._parent(i)
            idx[pq[i][0]], idx[pq[p][0]] = idx[pq[p][0]], idx[pq[i][0]]
            pq[i], pq[p] = pq[p], pq[i]
            i = p

    def _shiftDown(self, i, pq, idx):
        minIdx = i

        l = self._leftChild(i)
        if l < len(pq) and pq[l][1] < pq[minIdx][1]:
            minIdx = l

        r = self._rightChild(i)
        if r < len(pq) and pq[r][1] < pq[minIdx][1]:
            minIdx = r

        if minIdx != i:
            idx[pq[i][0]], idx[pq[minIdx][0]] = idx[pq[minIdx][0]], idx[pq[i][0]]
            pq[i], pq[minIdx] = pq[minIdx], pq[i]
            self._shiftDown(minIdx, pq, idx)

    def _leftChild(self, i):
        return i*2+1

    def _rightChild(self, i):
        return i*2+2

    def _parent(self, i):
        return (i-1)//2
