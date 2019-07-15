import unittest
from bellmanFord import BellmanFord

class BellmanFordTest (unittest.TestCase):
    def setUp(self):
        self.bf = BellmanFord()
        
        self.graph1 = [[0, 1, 4], [0, 2, 3]
                , [1, 2, -2], [1, 3, 4]
                , [2, 3, -3], [2, 4, 1]
                , [3, 4, 2]]
        self.graph2 = [[0, 1, -1], [0, 2, 4]
                , [1, 2, 3], [1, 3, 2], [1, 4, 2]
                , [3, 1, 1], [3, 2, 5]
                , [4, 3, -3]]
        self.graph3 = [[0, 1, 4], [0, 2, 2], [1, 3, -2], [3, 2, -3], [2, 1, 1], [2, 4, 4]]

    def test_bellmanFord(self):
        dist, prev = self.bf.run(self.graph1, 5, 0)
        self.assertEqual([0, 4, 2, -1, 1], dist)
        self.assertEqual([None, 0, 1, 2, 3], prev)
        
        dist, prev = self.bf.run(self.graph2, 5, 0)
        self.assertEqual([0, -1, 2, -2, 1], dist)
        self.assertEqual([None, 0, 1, 4, 1], prev)

        with self.assertRaises(Exception):
            self.bf.run(self.graph3, 5, 0)

if __name__ == '__main__':
    unittest.main()
