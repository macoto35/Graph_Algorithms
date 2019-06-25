import unittest
from easyStronglyConnectedComponent import EasyStronglyConnectedComponent
from basicStronglyConnectedComponent import BasicStronglyConnectedComponent
from enhancedStronglyConnectedComponent import EnhancedStronglyConnectedComponent

class StronglyConnectedComponentTest(unittest.TestCase):
    def setUp(self):
        self.scc1 = EasyStronglyConnectedComponent()
        self.scc2 = BasicStronglyConnectedComponent()
        self.scc3 = EnhancedStronglyConnectedComponent()
        self.adjList1 = [[1], [4, 5], [1], [0, 6], [0, 2, 7], [], [7], [8], [5, 7]]
        self.adjList2 = [[2,3],[0],[1],[4],[]]
    
    def test_easyScc(self):
        self.assertEqual([1, 1, 1, 2, 1, 3, 4, 5, 5], self.scc1.easyScc(self.adjList1))
        self.assertEqual([1, 1, 1, 2, 3], self.scc1.easyScc(self.adjList2))

    def test_basicScc(self):
        self.assertEqual([4, 4, 4, 5, 4, 1, 3, 2, 2], self.scc2.basicScc(self.adjList1))
        self.assertEqual([3, 3, 3, 2, 1], self.scc2.basicScc(self.adjList2))

    def test_enhancedScc(self):
        self.assertEqual([4, 4, 4, 5, 4, 1, 3, 2, 2], self.scc3.enhancedScc(self.adjList1))
        self.assertEqual([3, 3, 3, 2, 1], self.scc3.enhancedScc(self.adjList2))

if __name__ == '__main__':
    unittest.main()
