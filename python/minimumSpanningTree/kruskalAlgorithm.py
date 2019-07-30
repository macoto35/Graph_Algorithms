class KruskalAlgorithm:
    def run(self, graph, numOfVertex):
        self._init(numOfVertex)
        x = []

        for i in range(numOfVertex):
            self._makeSet(i)

        self._quickSort(graph, 0, len(graph)-1)

        for u, v, w in graph:
            if self._find(u) != self._find(v):
                self._union(u, v)
                x.append([u, v])

        return x

    def _init(self, numOfVertex):
        self.parent = [None] * numOfVertex
        self.rank = [None] * numOfVertex





    # Disjoint Set
    def _makeSet(self, i):
        self.parent[i] = i
        self.rank[i] = 0

    def _find(self, i):
        while i != self.parent[i]:
            i = self.parent[i]

        return self.parent[i]

    def _union(self, i, j):
        i_id = self._find(i)
        j_id = self._find(j)

        if i_id == j_id:
            return

        if self.rank[i_id] > self.rank[j_id]:
            self.parent[j_id] = self.parent[i_id]
        else:
            self.parent[i_id] = self.parent[j_id]
            if self.rank[i_id] == self.rank[j_id]:
            self.rank[j_id] += 1





    # Quick Sort
    def _quickSort(self, graph, st, ed):
        if st < ed:
            m1, m2 = self._partition(graph, st, ed)
            
            self._quickSort(graph, st, m1-1)
            self._quickSort(graph, m2+1, ed)

    def _partition(self, graph, st, ed):
        pivot = self._getPivot(graph, st, ed)
        m1 = m2 = st

        for i in range(st+1, ed+1):
            val = graph[i][2]
            if val <= pivot:
                if val < pivot:
                    self._swap(graph, m1, i)
                    m1 += 1
                m2 += 1
                self._swap(graph, m2, i)
        
        return [m1, m2]

    def _getPivot(self, graph, st, ed):
        mid = (st + ed) // 2
        self._swap(graph, mid, st)
        
        return graph[st][2]

        
    def _swap(self, graph, i, j):
            graph[i], graph[j] = graph[j], graph[i]



