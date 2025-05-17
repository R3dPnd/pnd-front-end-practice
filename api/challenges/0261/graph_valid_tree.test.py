import unittest
from typing import List
from graph_valid_tree import Solution


class TestValidTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_graph(self):
        """Test case for n=1 (single node)"""
        n = 1
        edges: List[List[int]] = []
        self.assertTrue(self.solution.validTree(n, edges))

    def test_simple_valid_tree(self):
        """Test case for a simple valid tree with 3 nodes"""
        n = 3
        edges = [[0, 1], [1, 2]]
        self.assertTrue(self.solution.validTree(n, edges))

    def test_simple_invalid_tree(self):
        """Test case for a graph with cycle (invalid tree)"""
        n = 3
        edges = [[0, 1], [1, 2], [2, 0]]
        self.assertFalse(self.solution.validTree(n, edges))

    def test_disconnected_graph(self):
        """Test case for disconnected graph (invalid tree)"""
        n = 4
        edges = [[0, 1], [2, 3]]
        self.assertFalse(self.solution.validTree(n, edges))

    def test_wrong_number_of_edges(self):
        """Test case where number of edges != n-1"""
        n = 4
        edges = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 2]]
        self.assertFalse(self.solution.validTree(n, edges))

    def test_complex_valid_tree(self):
        """Test case for a more complex valid tree"""
        n = 5
        edges = [[0, 1], [0, 2], [2, 3], [2, 4]]
        self.assertTrue(self.solution.validTree(n, edges))

    def test_complex_invalid_tree(self):
        """Test case for a more complex invalid tree with cycle"""
        n = 5
        edges = [[0, 1], [0, 2], [2, 3], [2, 4], [3, 4]]
        self.assertFalse(self.solution.validTree(n, edges))

    def test_self_loop(self):
        """Test case for graph with self-loop (invalid tree)"""
        n = 2
        edges = [[0, 0], [0, 1]]
        self.assertFalse(self.solution.validTree(n, edges))

if __name__ == '__main__':
    unittest.main()