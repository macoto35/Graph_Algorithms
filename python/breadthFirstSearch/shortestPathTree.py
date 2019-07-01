class ShortestPathTree:
    def reconstructPath(self, adjList, origin, dest):
        prev = self.bfs(adjList, origin)
        #print(prev, origin, dest)
        result = []

        if prev[dest] is None:
            return result

        while prev[dest] is not None:
            result.append(dest)
            dest = prev[dest]
        result.append(dest)

        return result

    def bfs(self, adjList, origin):
        dest = [None for i in range(len(adjList))]
        prev = [None for i in range(len(adjList))]
        dest[origin] = 0

        queue = [origin]

        while len(queue) != 0:
            u = queue.pop(0)

            for v in adjList[u]:
                if dest[v] is None:
                    dest[v] = dest[u] + 1
                    prev[v] = u
                    queue.append(v)

        return prev
