import unittest

from lc_z_bag import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution().bag(4, [3, 3, 1, 2], [15, 20, 30, 10]), 50)

    def test_2(self):
        self.assertEqual(Solution().bag(10, [3, 3, 1, 2, 5, 4], [15, 20, 30, 10, 45, 35]), 110)


if __name__ == "__main__":
    unittest.main()
