import unittest
from kruskalAlgorithm import KruskalAlgorithm
from primAlgorithm import PrimAlgorithm

class MinimumSpanningTreeTest(unittest.TestCase):
    def setUp(self):
        self.k = KruskalAlgorithm()
        self.p = PrimAlgorithm()

        self.graph1 = [[0, 1, 4]
                , [0, 3, 2]
                , [0, 4, 1]
                , [3, 4, 3]
                , [1, 4, 5]
                , [1, 2, 8]
                , [2, 5, 1]
                , [1, 5, 6]
                , [4, 5, 9]]

        self.graph2 = [
                  [[1, 2], [2, 4], [3, 1]]
                , [[0, 2], [3, 3]]
                , [[0, 4], [3, 5], [4, 8], [5, 6]]
                , [[0, 1], [1, 3], [2, 5], [5, 9]]
                , [[2, 8], [5, 1]]
                , [[2, 6], [3, 9], [4, 1]]]

    def test_kruskalAlgorithm(self):
        self.assertEqual([[0, 4], [2, 5], [0, 3], [0, 1], [1, 5]], self.k.run(self.graph1, 6))

    def test_primAlgorithm(self):
        cost, parent = self.p.run(self.graph2, 6)

        self.assertEqual([None, 0, 0, 0, 5, 2], parent)
        self.assertEqual([0, 2, 4, 1, 1, 6], cost)

if __name__ == '__main__':
    unittest.main()
