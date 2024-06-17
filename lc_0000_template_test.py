import unittest

from lc_0000_template import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution().template(), True)


if __name__ == "__main__":
    unittest.main()
