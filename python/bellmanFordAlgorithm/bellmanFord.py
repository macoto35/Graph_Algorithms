class BellmanFord:
    def relax(self, dist, prev, u, v, w):
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            prev[v] = u

    def run(self, graph, numOfVertex, s):
        dist = [float('inf') for i in range(numOfVertex)]
        prev = [None for i in range(numOfVertex)]
        dist[s] = 0

        for i in range(numOfVertex - 1):
            for u, v, w in graph:
                self.relax(dist, prev, u, v, w)

        for u, v, w in graph:
            if dist[v] > dist[u] + w:
                raise Exception('Graph contains negative weight cycle.')

        return [dist, prev]
