class BreadthFirstSearch:
    def run(self, adjList, origin):
        dist = [None for i in range(len(adjList))]
        dist[origin] = 0
        q = [origin]

        while len(q) != 0:
            u = q.pop(0)

            for v in adjList[u]:
                if dist[v] is None:
                    dist[v] = dist[u] + 1
                    q.append(v)

        return dist
