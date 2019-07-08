import unittest
from naiveDijkstra import NaiveDijkstra
from dijkstra import Dijkstra

class DijkstraTest(unittest.TestCase):
    def setUp(self):
        self.nd = NaiveDijkstra()
        self.d = Dijkstra()

        self.adjList = [[[1, 2], [2, 4]]
                        , [[0, 2], [2, 1], [3, 3], [4, 2]]
                        , [[0, 4], [1, 1], [3, 0], [4, 2]]
                        , [[1, 3], [2, 0], [4, 5], [5, 1]]
                        , [[1, 2], [2, 2], [3, 5], [5, 1]]
                        , [[3, 1], [4, 1]]]

    def testNaiveDijkstra(self):
        dist, prev = self.nd.run(self.adjList, 6, 0)

        self.assertEqual([0, 2, 3, 3, 4, 4], dist)
        self.assertEqual([None, 0, 1, 2, 1, 3], prev)

    def testDijkstra(self):
        dist, prev = self.d.run(self.adjList, 6, 0)

        self.assertEqual([0, 2, 3, 3, 4, 4], dist)
        self.assertEqual([None, 0, 1, 2, 1, 3], prev)

if __name__ == '__main__':
    unittest.main()
