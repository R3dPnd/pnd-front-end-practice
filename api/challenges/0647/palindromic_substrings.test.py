import unittest
from typing import List
from palindromic_substrings import Solution


class TestValidTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty(self):
        """Test case for n=1 (single node)"""
        self.assertEqual(self.solution.countSubstrings(""))

    def test_single_char(self):
        """Test case for a simple valid tree with 3 nodes"""
        self.assertEqual(self.solution.countSubstrings("a"))

    def test_simple(self):
        """Test case for a graph with cycle (invalid tree)"""
        self.assertEqual(self.solution.countSubstrings("abc"), 3)

    def test_all_a(self):
        """Test case for a graph with cycle (invalid tree)"""
        self.assertEqual(self.solution.countSubstrings("aaa"), 6)
    
    def test_all_a(self):
        """Test case for a graph with cycle (invalid tree)"""
        self.assertEqual(self.solution.countSubstrings("aba"), 4)

if __name__ == '__main__':
    unittest.main()