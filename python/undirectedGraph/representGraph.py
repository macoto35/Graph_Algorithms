class RepresentGraph:
    def getEdgeList(self, numOfVertex, numOfEdge, edges):
        return edges

    def isEdgeEdgeList(self, edges, st, ed):
        for u, v in edges:
            if (u == st and v == ed) or (u == ed and v == st):
                return True
        return False
    
    def getListEdgeEdgeList(self, edges):
        return edges

    def getListNeighbourEdgeList(self, edges, vertex):
        result = []
        
        for u, v in edges:
            if u == vertex:
                result.append(v)
            elif v == vertex:
                result.append(u)
        
        return result

    def getAdjMatrix(self, numOfVertex, numOfEdge, edges):
        matrix = [[0 for i in range(numOfVertex)] for j in range(numOfVertex)]

        for u, v in edges:
            matrix[u-1][v-1] = matrix[v-1][u-1] = 1
        
        return matrix
    
    def isEdgeAdjMatrix(self, matrix, st, ed):
        return matrix[st-1][ed-1]

    def getListEdgeAdjMatrix(self, matrix):
        result = []

        for u in range(len(matrix)):
            for v in range(len(matrix[u])):
                if matrix[u][v] == 1 and u < v:
                    result.append([u+1, v+1])
        
        return result

    def getListNeighbourAdjMatrix(self, matrix, vertex):
        result = []
        idx = 1

        for v in matrix[vertex-1]:
            if v == 1:
                result.append(idx)
            idx += 1
        
        return result

    def getAdjList(self, numOfVertex, numOfEdge, edges):
        adjList = [[] for i in range(numOfVertex)]

        for u, v in edges:
            adjList[u-1].append(v)
            adjList[v-1].append(u)
        
        return adjList
    
    def isEdgeAdjList(self, adjList, st, ed):
        for v in adjList[st - 1]:
            if v == ed:
                return True
        return False

    def getListEdgeAdjList(self, adjList):
        result = []

        for u in range(len(adjList)):
            for v in adjList[u]:    
                if u+1 < v:
                    result.append([u+1, v])
        
        return result
    
    def getListNeighbourAdjList(self, adjList, vertex):
        return adjList[vertex - 1]
