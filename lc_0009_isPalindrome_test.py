import unittest

from lc_0009_isPalindrome import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution().isPalindrome(121), True)

    def test_2(self):
        self.assertEqual(Solution().isPalindrome(-121), False)

    def test_3(self):
        self.assertEqual(Solution().isPalindrome(10), False)

    def test_4(self):
        self.assertEqual(Solution().isPalindrome(22), True)

    def test_5(self):
        self.assertEqual(Solution().isPalindrome(12521), True)


if __name__ == "__main__":
    unittest.main()
