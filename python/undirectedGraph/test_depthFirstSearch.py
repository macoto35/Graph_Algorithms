import unittest
from depthFirstSearch import DepthFirstSearch
from connectedComponent import ConnectedComponent
from prePostVisit import PrePostVisit

class DepthFirstSearchTest(unittest.TestCase):
    def setUp(self):
        self.numOfVertex = 9
        self.dfs = DepthFirstSearch(self.numOfVertex)
        self.cc = ConnectedComponent(self.numOfVertex)
        self.pp = PrePostVisit(self.numOfVertex)
        self.adjList = [[1, 2, 3], [0, 2], [0, 1], [0], [5], [4], [7, 8], [6, 8], [6, 7]]

    def test_explore(self):
        self.dfs.explore(self.adjList, 0)
        self.assertEqual([True, True, True, True, False, False, False, False, False], self.dfs.getVisited())
            
        self.dfs.initVisited(self.numOfVertex)
        self.dfs.explore(self.adjList, 1)
        self.assertEqual([True, True, True, True, False, False, False, False, False], self.dfs.getVisited())
            
        self.dfs.initVisited(self.numOfVertex)
        self.dfs.explore(self.adjList, 2)
        self.assertEqual([True, True, True, True, False, False, False, False, False], self.dfs.getVisited())
            
        self.dfs.initVisited(self.numOfVertex)
        self.dfs.explore(self.adjList, 3)
        self.assertEqual([True, True, True, True, False, False, False, False, False], self.dfs.getVisited())
            
        self.dfs.initVisited(self.numOfVertex)
        self.dfs.explore(self.adjList, 4)
        self.assertEqual([False, False, False, False, True, True, False, False, False], self.dfs.getVisited())
            
        self.dfs.initVisited(self.numOfVertex)
        self.dfs.explore(self.adjList, 5)
        self.assertEqual([False, False, False, False, True, True, False, False, False], self.dfs.getVisited())
            
        self.dfs.initVisited(self.numOfVertex)
        self.dfs.explore(self.adjList, 6)
        self.assertEqual([False, False, False, False, False, False, True, True, True], self.dfs.getVisited())
            
        self.dfs.initVisited(self.numOfVertex)
        self.dfs.explore(self.adjList, 7)
        self.assertEqual([False, False, False, False, False, False, True, True, True], self.dfs.getVisited())
            
        self.dfs.initVisited(self.numOfVertex)
        self.dfs.explore(self.adjList, 8)
        self.assertEqual([False, False, False, False, False, False, True, True, True], self.dfs.getVisited())

    def test_depthFirstSearch(self):
        self.dfs.depthFirstSearch(self.adjList, self.numOfVertex)
        self.assertEqual([True for i in range(self.numOfVertex)], self.dfs.getVisited())

    def test_connectedComponent(self):
        self.cc.connectedComponentDFS(self.adjList, self.numOfVertex)
        self.assertEqual([1, 1, 1, 1, 2, 2, 3, 3, 3], self.cc.getConnectedComponent())

    def test_prePostVisit(self):
        self.pp.prePostVisitCCDFS(self.adjList, self.numOfVertex)
        
        arr = self.pp.getPrePostVisit()
        self.assertEqual([1, 8], arr[0])
        self.assertEqual([2, 5], arr[1])
        self.assertEqual([3, 4], arr[2])
        self.assertEqual([6, 7], arr[3])
        self.assertEqual([9, 12], arr[4])
        self.assertEqual([10, 11], arr[5])
        self.assertEqual([13, 18], arr[6])
        self.assertEqual([14, 17], arr[7])
        self.assertEqual([15, 16], arr[8])

if __name__ == '__main__':
    unittest.main()
