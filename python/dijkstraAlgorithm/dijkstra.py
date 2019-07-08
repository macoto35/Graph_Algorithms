class Dijkstra:
    def run(self, adjList, numOfVertex, origin):
        dist = [float('inf') for i in range(numOfVertex)] 
        dist[origin] = 0
       
        prev = [None for i in range(numOfVertex)]

        idxes = [i for i in range(numOfVertex)]
        pq = self.createMinPQ(numOfVertex, origin, idxes)

        while len(pq) != 0:
            u = self.extractMin(pq, idxes)

            for v, w in adjList[u[0]]:
                if dist[v] > dist[u[0]] + w:
                    dist[v] = dist[u[0]] + w
                    prev[v] = u[0]
                    self.changePriority(v, dist, pq, idxes)
        
        return [dist, prev]

    def createMinPQ(self, numOfVertex, origin, idxes):
        pq = [[i, float('inf')] for i in range(numOfVertex)]

        pq[0] = [origin, 0]
        pq[origin][0] = 0
        
        idxes[0] = origin
        idxes[origin] = 0

        return pq

    def extractMin(self, pq, idxes):
        size = len(pq)

        result = pq[0]
        idxes[result[0]] = None

        pq[0] = pq[size - 1]
        idxes[pq[0][0]] = 0
        pq.pop()
        
        self.shiftDown(0, pq, idxes)

        return result

    def shiftUp(self, i, pq, idxes):
        while i > 0 and pq[i][1] < pq[self.parent(i)][1]:
            p = self.parent(i)
            pq[i], pq[p] = pq[p], pq[i]
            idxes[pq[i][0]] = i
            idxes[pq[p][0]] = p
            i = p

    def shiftDown(self, i, pq, idxes):
        minIdx = i

        if i < len(pq):
            l = self.leftChild(i)
            if l < len(pq) and pq[l][1] < pq[minIdx][1]:
                minIdx = l

            r = self.rightChild(i)
            if r < len(pq) and pq[r][1] < pq[minIdx][1]:
                minIdx = r

            if i != minIdx:
                pq[i], pq[minIdx] = pq[minIdx], pq[i]
                idxes[pq[i][0]] = i
                idxes[pq[minIdx][0]] = minIdx
                self.shiftDown(minIdx, pq, idxes)

    def changePriority(self, v, dist, pq, idxes):
        i = idxes[v]

        oldp = pq[i][1]
        newp = pq[i][1] = dist[v]

        if oldp > newp:
            self.shiftUp(i, pq, idxes)
        else:
            self.shiftDown(i, pq, idxes)

    def parent(self, i):
        return (i - 1) // 2

    def leftChild(self, i):
        return (i * 2) + 1

    def rightChild(self, i):
        return (i * 2) + 2
