class FindingSink:
    def __init__(self):
        pass

    def linearOrder(self, adjList):
        result = []
        numOfVertex = len(adjList)

        while True:
            # follow a path until cannot extend. find sink v.
            v = 0
            while len(adjList[v]) != 0:
                v = adjList[v][0]

            # put sink v to result
            result.insert(0, v)
            
            if v == 0:
                break

            # remove sink v from G
            for arr in adjList:
                try:
                    arr.remove(v)
                except ValueError:
                    continue
        
        return result
