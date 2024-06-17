import unittest

from lc_0051_solveNQueens import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            Solution().solveNQueens(4), [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]
        )


if __name__ == "__main__":
    unittest.main()
