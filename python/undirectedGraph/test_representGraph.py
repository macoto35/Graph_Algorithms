import unittest
from representGraph import RepresentGraph

class RepresentGraphTest(unittest.TestCase):
    def setUp(self):
        self.rg = RepresentGraph()

    def test_edgeList(self):
        edges = self.rg.getEdgeList(4, 4, [[1, 2],[1, 3],[1, 4],[3, 4]])
        
        self.assertEqual(True, self.rg.isEdgeEdgeList(edges, 1, 2))
        self.assertEqual(True, self.rg.isEdgeEdgeList(edges, 1, 3))
        self.assertEqual(True, self.rg.isEdgeEdgeList(edges, 1, 4))
        self.assertEqual(True, self.rg.isEdgeEdgeList(edges, 2, 1))
        self.assertEqual(False, self.rg.isEdgeEdgeList(edges, 2, 3))
        self.assertEqual(False, self.rg.isEdgeEdgeList(edges, 2, 4))
        self.assertEqual(True, self.rg.isEdgeEdgeList(edges, 3, 1))
        self.assertEqual(False, self.rg.isEdgeEdgeList(edges, 3, 2))
        self.assertEqual(True, self.rg.isEdgeEdgeList(edges, 3, 4))
        self.assertEqual(True, self.rg.isEdgeEdgeList(edges, 4, 1))
        self.assertEqual(False, self.rg.isEdgeEdgeList(edges, 4, 2))
        self.assertEqual(True, self.rg.isEdgeEdgeList(edges, 4, 3))

        self.assertEqual(edges, self.rg.getListEdgeEdgeList(edges))

        self.assertEqual([2, 3, 4], self.rg.getListNeighbourEdgeList(edges, 1))
        self.assertEqual([1], self.rg.getListNeighbourEdgeList(edges, 2))
        self.assertEqual([1, 4], self.rg.getListNeighbourEdgeList(edges, 3))
        self.assertEqual([1, 3], self.rg.getListNeighbourEdgeList(edges, 4))

    def test_adjMatrix(self):
        edges = [[1, 2],[1, 3],[1, 4],[3, 4]]
        matrix = self.rg.getAdjMatrix(4, 4, edges)
        self.assertEqual([[0, 1, 1, 1],[1, 0, 0, 0],[1, 0, 0, 1], [1, 0, 1, 0]], matrix)
        
        self.assertEqual(True, self.rg.isEdgeAdjMatrix(matrix, 1, 2))
        self.assertEqual(True, self.rg.isEdgeAdjMatrix(matrix, 1, 3))
        self.assertEqual(True, self.rg.isEdgeAdjMatrix(matrix, 1, 4))
        self.assertEqual(True, self.rg.isEdgeAdjMatrix(matrix, 2, 1))
        self.assertEqual(False, self.rg.isEdgeAdjMatrix(matrix, 2, 3))
        self.assertEqual(False, self.rg.isEdgeAdjMatrix(matrix, 2, 4))
        self.assertEqual(True, self.rg.isEdgeAdjMatrix(matrix, 3, 1))
        self.assertEqual(False, self.rg.isEdgeAdjMatrix(matrix, 3, 2))
        self.assertEqual(True, self.rg.isEdgeAdjMatrix(matrix, 3, 4))
        self.assertEqual(True, self.rg.isEdgeAdjMatrix(matrix, 4, 1))
        self.assertEqual(False, self.rg.isEdgeAdjMatrix(matrix, 4, 2))
        self.assertEqual(True, self.rg.isEdgeAdjMatrix(matrix, 4, 3))

        self.assertEqual(edges, self.rg.getListEdgeAdjMatrix(matrix))

        self.assertEqual([2, 3, 4], self.rg.getListNeighbourAdjMatrix(matrix, 1))
        self.assertEqual([1], self.rg.getListNeighbourAdjMatrix(matrix, 2))
        self.assertEqual([1, 4], self.rg.getListNeighbourAdjMatrix(matrix, 3))
        self.assertEqual([1, 3], self.rg.getListNeighbourAdjMatrix(matrix, 4))

    def test_adjList(self):
        edges = [[1, 2],[1, 3],[1, 4],[3, 4]]
        adjList = self.rg.getAdjList(4, 4, edges)
        self.assertEqual([[2, 3, 4],[1],[1, 4], [1, 3]], adjList)
        
        self.assertEqual(True, self.rg.isEdgeAdjList(adjList, 1, 2))
        self.assertEqual(True, self.rg.isEdgeAdjList(adjList, 1, 3))
        self.assertEqual(True, self.rg.isEdgeAdjList(adjList, 1, 4))
        self.assertEqual(True, self.rg.isEdgeAdjList(adjList, 2, 1))
        self.assertEqual(False, self.rg.isEdgeAdjList(adjList, 2, 3))
        self.assertEqual(False, self.rg.isEdgeAdjList(adjList, 2, 4))
        self.assertEqual(True, self.rg.isEdgeAdjList(adjList, 3, 1))
        self.assertEqual(False, self.rg.isEdgeAdjList(adjList, 3, 2))
        self.assertEqual(True, self.rg.isEdgeAdjList(adjList, 3, 4))
        self.assertEqual(True, self.rg.isEdgeAdjList(adjList, 4, 1))
        self.assertEqual(False, self.rg.isEdgeAdjList(adjList, 4, 2))
        self.assertEqual(True, self.rg.isEdgeAdjList(adjList, 4, 3))
        
        self.assertEqual(edges, self.rg.getListEdgeAdjList(adjList))
        
        self.assertEqual([2, 3, 4], self.rg.getListNeighbourAdjList(adjList, 1))
        self.assertEqual([1], self.rg.getListNeighbourAdjList(adjList, 2))
        self.assertEqual([1, 4], self.rg.getListNeighbourAdjList(adjList, 3))
        self.assertEqual([1, 3], self.rg.getListNeighbourAdjList(adjList, 4))
        

if __name__ == '__main__':
	unittest.main()
