import unittest
from findingExitFromMaze import FindingExitFromMaze

class findingExitFromMazeTest(unittest.TestCase):
    def setUp(self):
        self.findingExit = FindingExitFromMaze()

    def test_dfsAdjMatrix(self):
        n = m = 4
        edges = [[1, 2], [3, 2], [4, 3], [1, 4]]
        self.assertEqual(self.findingExit.adjMatrixIter(n, m, edges, 1, 4), 1)
        self.assertEqual(self.findingExit.adjMatrixRecur(n, m, edges, 1, 4), 1)

        n = 4
        m = 2
        edges = [[1, 2], [3, 2]]
        self.assertEqual(self.findingExit.adjMatrixIter(n, m, edges, 1, 4), 0)
        self.assertEqual(self.findingExit.adjMatrixRecur(n, m, edges, 1, 4), 0)

        n = 6
        m = 4
        edges = [[1, 2], [1, 3], [1, 4], [5, 6]]
        self.assertEqual(self.findingExit.adjMatrixIter(n, m, edges, 2, 4), 1)
        self.assertEqual(self.findingExit.adjMatrixRecur(n, m, edges, 2, 4), 1)
        self.assertEqual(self.findingExit.adjMatrixIter(n, m, edges, 3, 5), 0)
        self.assertEqual(self.findingExit.adjMatrixRecur(n, m, edges, 3, 5), 0)


    def test_dfsAdjList(self):
        n = m = 4
        edges = [[1, 2], [3, 2], [4, 3], [1, 4]]
        self.assertEqual(self.findingExit.adjListIter(n, m, edges, 1, 4), 1)
        self.assertEqual(self.findingExit.adjListRecur(n, m, edges, 1, 4), 1)

        n = 4
        m = 2
        edges = [[1, 2], [3, 2]]
        self.assertEqual(self.findingExit.adjListIter(n, m, edges, 1, 4), 0)
        self.assertEqual(self.findingExit.adjListRecur(n, m, edges, 1, 4), 0)
        
        n = 6
        m = 4
        edges = [[1, 2], [1, 3], [1, 4], [5, 6]]
        self.assertEqual(self.findingExit.adjListIter(n, m, edges, 2, 4), 1)
        self.assertEqual(self.findingExit.adjListRecur(n, m, edges, 2, 4), 1)
        self.assertEqual(self.findingExit.adjListIter(n, m, edges, 3, 5), 0)
        self.assertEqual(self.findingExit.adjListRecur(n, m, edges, 3, 5), 0)

if __name__ == '__main__':
    unittest.main()
