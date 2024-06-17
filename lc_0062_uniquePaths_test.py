import unittest

from lc_0062_uniquePaths import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution().uniquePaths(3, 7), 28)

    def test_2(self):
        self.assertEqual(Solution().uniquePaths(3, 2), 3)

    def test_3(self):
        self.assertEqual(Solution().uniquePaths(7, 3), 28)

    def test_4(self):
        self.assertEqual(Solution().uniquePaths(3, 3), 6)

    def test_5(self):
        self.assertEqual(Solution().uniquePaths(23, 12), 193536720)


if __name__ == "__main__":
    unittest.main()
