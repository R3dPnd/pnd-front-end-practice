import unittest
from alien_dictionary import Solution

class TestAlienDictionary(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_input(self):
        self.assertEqual(self.solution.alienOrder([]), "")

    def test_single_word(self):
        self.assertEqual(self.solution.alienOrder(["abc"]), "abc")

    def test_simple_order(self):
        words = ["wrt", "wrf", "er", "ett", "rftt"]
        self.assertEqual(self.solution.alienOrder(words), "wertf")

    def test_invalid_order(self):
        words = ["abc", "ab"]
        self.assertEqual(self.solution.alienOrder(words), "")

    def test_cyclic_dependency(self):
        words = ["z", "x", "z"]
        self.assertEqual(self.solution.alienOrder(words), "")

    def test_multiple_possible_orders(self):
        words = ["z", "x"]
        result = self.solution.alienOrder(words)
        self.assertTrue(result in ["zx", "xz"])

    def test_longer_words(self):
        words = ["apple", "app"]
        self.assertEqual(self.solution.alienOrder(words), "")

    def test_same_prefix(self):
        words = ["abc", "abd"]
        self.assertEqual(self.solution.alienOrder(words), "abcd")

    def test_complex_case(self):
        words = ["wrt", "wrf", "er", "ett", "rftt", "te"]
        result = self.solution.alienOrder(words)
        self.assertTrue(len(result) > 0)
        self.assertTrue(all(c in result for c in "wertf"))

    def test_duplicate_words(self):
        words = ["abc", "abc"]
        self.assertEqual(self.solution.alienOrder(words), "abc")

if __name__ == '__main__':
    unittest.main() 