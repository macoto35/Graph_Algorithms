import unittest
from breadthFirstSearch import BreadthFirstSearch

class BfsTest (unittest.TestCase):
    def setUp(self):
        self.bfs = BreadthFirstSearch()
        
        self.undirectedAdjList1 = [[1, 5], [0, 2], [1, 5], [4, 5], [3, 5], [0, 2, 3, 4]]
        self.undirectedAdjList2 = [[1, 2, 3, 4, 5], [0, 2, 4, 5, 8], [0, 1, 3, 5, 6], [0, 2, 4, 6, 7], [0, 1, 3, 7, 8], [0, 1, 2, 6, 8], [2, 3, 5, 7], [3, 4, 6, 8], [1, 4, 5, 7], []]

        self.directedAdjList1 = [[5], [0, 2], [5], [5], [3], [4]]
        self.directedAdjList2 = [[1, 2, 3, 4], [0, 2, 5, 8], [3, 5, 6], [4, 6, 7], [1, 7, 8], [0, 6], [7], [8], [5], []]
    
    def test_undirectedBfs(self):
        self.assertEqual([0, 1, 2, 2, 2, 1], self.bfs.run(self.undirectedAdjList1, 0))
        self.assertEqual([1, 0, 1, 3, 3, 2], self.bfs.run(self.undirectedAdjList1, 1))
        self.assertEqual([2, 1, 0, 2, 2, 1], self.bfs.run(self.undirectedAdjList1, 2))
        self.assertEqual([2, 3, 2, 0, 1, 1], self.bfs.run(self.undirectedAdjList1, 3))
        self.assertEqual([2, 3, 2, 1, 0, 1], self.bfs.run(self.undirectedAdjList1, 4))
        self.assertEqual([1, 2, 1, 1, 1, 0], self.bfs.run(self.undirectedAdjList1, 5))

        self.assertEqual([0, 1, 1, 1, 1, 1, 2, 2, 2, None], self.bfs.run(self.undirectedAdjList2, 0))

    def test_directedBfs(self):
        self.assertEqual([0, None, None, 3, 2, 1], self.bfs.run(self.directedAdjList1, 0))
        self.assertEqual([1, 0, 1, 4, 3, 2], self.bfs.run(self.directedAdjList1, 1))
        self.assertEqual([None, None, 0, 3, 2, 1], self.bfs.run(self.directedAdjList1, 2))
        self.assertEqual([None, None, None, 0, 2, 1], self.bfs.run(self.directedAdjList1, 3))
        self.assertEqual([None, None, None, 1, 0, 2], self.bfs.run(self.directedAdjList1, 4))
        self.assertEqual([None, None, None, 2, 1, 0], self.bfs.run(self.directedAdjList1, 5))
        
        self.assertEqual([0, 1, 1, 1, 1, 2, 2, 2, 2, None], self.bfs.run(self.directedAdjList2, 0))

if __name__ == '__main__':
    unittest.main()
