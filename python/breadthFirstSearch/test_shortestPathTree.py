import unittest
from shortestPathTree import ShortestPathTree

class ShortestPathTreeTest(unittest.TestCase):
    def setUp(self):
        self.spt = ShortestPathTree()

        self.undirectedAdjList1 = [[1, 5], [0, 2], [1, 5], [4, 5], [3, 5], [0, 2, 3, 4]]
        self.undirectedAdjList2 = [[1, 2, 3, 4, 5], [0, 2, 4, 5, 8], [0, 1, 3, 5, 6], [0, 2, 4, 6, 7], [0, 1, 3, 7, 8], [0, 1, 2, 6, 8], [2, 3, 5, 7], [3, 4, 6, 8], [1, 4, 5, 7], []]

        self.directedAdjList1 = [[5], [0, 2], [5], [5], [3], [4]]
        self.directedAdjList2 = [[1, 2, 3, 4], [0, 2, 5, 8], [3, 5, 6], [4, 6, 7], [1, 7, 8], [0, 6], [7], [8], [5], []]

    def test_spt_undirectedAdjList(self):
        # dist: [0, 1, 2, 2, 2, 1] origin: 0
        self.assertEqual([], self.spt.reconstructPath(self.undirectedAdjList1, 0, 0))
        self.assertEqual([1, 0], self.spt.reconstructPath(self.undirectedAdjList1, 0, 1))
        self.assertEqual([2, 1, 0], self.spt.reconstructPath(self.undirectedAdjList1, 0, 2))
        self.assertEqual([3, 5, 0], self.spt.reconstructPath(self.undirectedAdjList1, 0, 3))
        self.assertEqual([4, 5, 0], self.spt.reconstructPath(self.undirectedAdjList1, 0, 4))
        self.assertEqual([5, 0], self.spt.reconstructPath(self.undirectedAdjList1, 0, 5))

        # dist: [1, 0, 1, 3, 3, 2] origin: 1
        self.assertEqual([0, 1], self.spt.reconstructPath(self.undirectedAdjList1, 1, 0))
        self.assertEqual([], self.spt.reconstructPath(self.undirectedAdjList1, 1, 1))
        self.assertEqual([2, 1], self.spt.reconstructPath(self.undirectedAdjList1, 1, 2))
        self.assertEqual([3, 5, 0, 1], self.spt.reconstructPath(self.undirectedAdjList1, 1, 3))
        self.assertEqual([4, 5, 0, 1], self.spt.reconstructPath(self.undirectedAdjList1, 1, 4))
        self.assertEqual([5, 0, 1], self.spt.reconstructPath(self.undirectedAdjList1, 1, 5))
        
        # dist: [2, 1, 0, 2, 2, 1] origin: 2
        self.assertEqual([0, 1, 2], self.spt.reconstructPath(self.undirectedAdjList1, 2, 0))
        self.assertEqual([1, 2], self.spt.reconstructPath(self.undirectedAdjList1, 2, 1))
        self.assertEqual([], self.spt.reconstructPath(self.undirectedAdjList1, 2, 2))
        self.assertEqual([3, 5, 2], self.spt.reconstructPath(self.undirectedAdjList1, 2, 3))
        self.assertEqual([4, 5, 2], self.spt.reconstructPath(self.undirectedAdjList1, 2, 4))
        self.assertEqual([5, 2], self.spt.reconstructPath(self.undirectedAdjList1, 2, 5))
        
        # dist: [2, 3, 2, 0, 1, 1] origin: 3
        self.assertEqual([0, 5, 3], self.spt.reconstructPath(self.undirectedAdjList1, 3, 0))
        self.assertEqual([1, 0, 5, 3], self.spt.reconstructPath(self.undirectedAdjList1, 3, 1))
        self.assertEqual([2, 5, 3], self.spt.reconstructPath(self.undirectedAdjList1, 3, 2))
        self.assertEqual([], self.spt.reconstructPath(self.undirectedAdjList1, 3, 3))
        self.assertEqual([4, 3], self.spt.reconstructPath(self.undirectedAdjList1, 3, 4))
        self.assertEqual([5, 3], self.spt.reconstructPath(self.undirectedAdjList1, 3, 5))
        
        # dist: [2, 3, 2, 1, 0, 1] origin: 4
        self.assertEqual([0, 5, 4], self.spt.reconstructPath(self.undirectedAdjList1, 4, 0))
        self.assertEqual([1, 0, 5, 4], self.spt.reconstructPath(self.undirectedAdjList1, 4, 1))
        self.assertEqual([2, 5, 4], self.spt.reconstructPath(self.undirectedAdjList1, 4, 2))
        self.assertEqual([3, 4], self.spt.reconstructPath(self.undirectedAdjList1, 4, 3))
        self.assertEqual([], self.spt.reconstructPath(self.undirectedAdjList1, 4, 4))
        self.assertEqual([5, 4], self.spt.reconstructPath(self.undirectedAdjList1, 4, 5))
        
        # dist: [1, 2, 1, 1, 1, 0] origin: 5
        self.assertEqual([0, 5], self.spt.reconstructPath(self.undirectedAdjList1, 5, 0))
        self.assertEqual([1, 0, 5], self.spt.reconstructPath(self.undirectedAdjList1, 5, 1))
        self.assertEqual([2, 5], self.spt.reconstructPath(self.undirectedAdjList1, 5, 2))
        self.assertEqual([3, 5], self.spt.reconstructPath(self.undirectedAdjList1, 5, 3))
        self.assertEqual([4, 5], self.spt.reconstructPath(self.undirectedAdjList1, 5, 4))
        self.assertEqual([], self.spt.reconstructPath(self.undirectedAdjList1, 5, 5))

        # dist: [0, 1, 1, 1, 1, 1, 2, 2, 2, None] origin: 0
        self.assertEqual([], self.spt.reconstructPath(self.undirectedAdjList2, 0, 0))
        self.assertEqual([1, 0], self.spt.reconstructPath(self.undirectedAdjList2, 0, 1))
        self.assertEqual([2, 0], self.spt.reconstructPath(self.undirectedAdjList2, 0, 2))
        self.assertEqual([3, 0], self.spt.reconstructPath(self.undirectedAdjList2, 0, 3))
        self.assertEqual([4, 0], self.spt.reconstructPath(self.undirectedAdjList2, 0, 4))
        self.assertEqual([5, 0], self.spt.reconstructPath(self.undirectedAdjList2, 0, 5))
        self.assertEqual([6, 2, 0], self.spt.reconstructPath(self.undirectedAdjList2, 0, 6))
        self.assertEqual([7, 3, 0], self.spt.reconstructPath(self.undirectedAdjList2, 0, 7))
        self.assertEqual([8, 1, 0], self.spt.reconstructPath(self.undirectedAdjList2, 0, 8))
        self.assertEqual([], self.spt.reconstructPath(self.undirectedAdjList2, 0, 9))

    def test_spt_directedAdjList(self):
        # dist: [0, None, None, 3, 2, 1] origin: 0
        self.assertEqual([], self.spt.reconstructPath(self.directedAdjList1, 0, 0))
        self.assertEqual([], self.spt.reconstructPath(self.directedAdjList1, 0, 1))
        self.assertEqual([], self.spt.reconstructPath(self.directedAdjList1, 0, 2))
        self.assertEqual([3, 4, 5, 0], self.spt.reconstructPath(self.directedAdjList1, 0, 3))
        self.assertEqual([4, 5, 0], self.spt.reconstructPath(self.directedAdjList1, 0, 4))
        self.assertEqual([5, 0], self.spt.reconstructPath(self.directedAdjList1, 0, 5))

        # dist: [1, 0, 1, 4, 3, 2] origin: 1
        self.assertEqual([0, 1], self.spt.reconstructPath(self.directedAdjList1, 1, 0))
        self.assertEqual([], self.spt.reconstructPath(self.directedAdjList1, 1, 1))
        self.assertEqual([2, 1], self.spt.reconstructPath(self.directedAdjList1, 1, 2))
        self.assertEqual([3, 4, 5, 0, 1], self.spt.reconstructPath(self.directedAdjList1, 1, 3))
        self.assertEqual([4, 5, 0, 1], self.spt.reconstructPath(self.directedAdjList1, 1, 4))
        self.assertEqual([5, 0, 1], self.spt.reconstructPath(self.directedAdjList1, 1, 5))
        
        # dist: [None, None, 0, 3, 2, 1] origin: 2
        self.assertEqual([], self.spt.reconstructPath(self.directedAdjList1, 2, 0))
        self.assertEqual([], self.spt.reconstructPath(self.directedAdjList1, 2, 1))
        self.assertEqual([], self.spt.reconstructPath(self.directedAdjList1, 2, 2))
        self.assertEqual([3, 4, 5, 2], self.spt.reconstructPath(self.directedAdjList1, 2, 3))
        self.assertEqual([4, 5, 2], self.spt.reconstructPath(self.directedAdjList1, 2, 4))
        self.assertEqual([5, 2], self.spt.reconstructPath(self.directedAdjList1, 2, 5))
        
        # dist: [None, None, None, 0, 2, 1] origin: 3
        self.assertEqual([], self.spt.reconstructPath(self.directedAdjList1, 3, 0))
        self.assertEqual([], self.spt.reconstructPath(self.directedAdjList1, 3, 1))
        self.assertEqual([], self.spt.reconstructPath(self.directedAdjList1, 3, 2))
        self.assertEqual([], self.spt.reconstructPath(self.directedAdjList1, 3, 3))
        self.assertEqual([4, 5, 3], self.spt.reconstructPath(self.directedAdjList1, 3, 4))
        self.assertEqual([5, 3], self.spt.reconstructPath(self.directedAdjList1, 3, 5))
        
        # dist: [None, None, None, 1, 0, 2] origin: 4
        self.assertEqual([], self.spt.reconstructPath(self.directedAdjList1, 4, 0))
        self.assertEqual([], self.spt.reconstructPath(self.directedAdjList1, 4, 1))
        self.assertEqual([], self.spt.reconstructPath(self.directedAdjList1, 4, 2))
        self.assertEqual([3, 4], self.spt.reconstructPath(self.directedAdjList1, 4, 3))
        self.assertEqual([], self.spt.reconstructPath(self.directedAdjList1, 4, 4))
        self.assertEqual([5, 3, 4], self.spt.reconstructPath(self.directedAdjList1, 4, 5))
        
        # dist: [None, None, None, 2, 1, 0] origin: 5
        self.assertEqual([], self.spt.reconstructPath(self.directedAdjList1, 5, 0))
        self.assertEqual([], self.spt.reconstructPath(self.directedAdjList1, 5, 1))
        self.assertEqual([], self.spt.reconstructPath(self.directedAdjList1, 5, 2))
        self.assertEqual([3, 4, 5], self.spt.reconstructPath(self.directedAdjList1, 5, 3))
        self.assertEqual([4, 5], self.spt.reconstructPath(self.directedAdjList1, 5, 4))
        self.assertEqual([], self.spt.reconstructPath(self.directedAdjList1, 5, 5))

        # dist: [0, 1, 1, 1, 1, 2, 2, 2, 2, None] origin: 0
        self.assertEqual([], self.spt.reconstructPath(self.directedAdjList2, 0, 0))
        self.assertEqual([1, 0], self.spt.reconstructPath(self.directedAdjList2, 0, 1))
        self.assertEqual([2, 0], self.spt.reconstructPath(self.directedAdjList2, 0, 2))
        self.assertEqual([3, 0], self.spt.reconstructPath(self.directedAdjList2, 0, 3))
        self.assertEqual([4, 0], self.spt.reconstructPath(self.directedAdjList2, 0, 4))
        self.assertEqual([5, 1, 0], self.spt.reconstructPath(self.directedAdjList2, 0, 5))
        self.assertEqual([6, 2, 0], self.spt.reconstructPath(self.directedAdjList2, 0, 6))
        self.assertEqual([7, 3, 0], self.spt.reconstructPath(self.directedAdjList2, 0, 7))
        self.assertEqual([8, 1, 0], self.spt.reconstructPath(self.directedAdjList2, 0, 8))
        self.assertEqual([], self.spt.reconstructPath(self.directedAdjList2, 0, 9))

if __name__ == '__main__':
    unittest.main()
