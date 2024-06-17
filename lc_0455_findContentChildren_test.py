import unittest

from lc_0455_findContentChildren import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution().findContentChildren([1, 2, 7, 10], [1, 3, 5, 9]), 3)

    def test_2(self):
        self.assertEqual(Solution().findContentChildren([1, 2, 3], [1, 1, 3, 4]), 3)

    def test_3(self):
        self.assertEqual(Solution().findContentChildren([4, 2, 3], [3, 1, 2, 8]), 3)

    def test_4(self):
        self.assertEqual(Solution().findContentChildren([1, 2], [1, 2, 3]), 2)

    def test_5(self):
        self.assertEqual(Solution().findContentChildren([1, 2, 3], []), 0)


if __name__ == "__main__":
    unittest.main()
