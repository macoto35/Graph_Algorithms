class NaiveDijkstra:
    def run(self, adjList, numOfVertex, origin):
        dist = [float('inf') for i in range(numOfVertex)]
        prev = [None for i in range(numOfVertex)]

        dist[origin] = 0

        for u in range(numOfVertex):
            for v, w in adjList[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    prev[v] = u

        return [dist, prev]

