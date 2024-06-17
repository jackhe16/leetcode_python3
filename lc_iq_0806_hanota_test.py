import unittest

from lc_iq_0806_hanota import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        A = list(range(3, -1, -1))
        B = []
        C = []
        Solution().hanota(A, B, C)
        self.assertEqual(C, list(range(3, -1, -1)))


if __name__ == "__main__":
    unittest.main()
