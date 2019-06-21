import unittest
from findingSink import FindingSink

class FindingSinkTest(unittest.TestCase):
    def setUp(self):
        self.fs = FindingSink()
        self.adjList = [[1, 3, 4], [2], [3], [], [3]]

    def test_linearOrder(self):
        self.assertEqual([0, 4, 1, 2, 3], self.fs.linearOrder(self.adjList))

if __name__ == '__main__':
    unittest.main()
