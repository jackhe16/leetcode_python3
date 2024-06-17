#
# @lc app=leetcode.cn id=9 lang=python3
#


# @lc code=start


class Solution:
    # def isPalindrome(self, x: int) -> bool:
    #     s = list(str(x))

    #     while len(s) > 1:
    #         if s.pop(0) != s.pop():
    #             return False

    #     return True

    # def isPalindrome(self, x: int) -> bool:
    #     s = list(str(x))

    #     l = 0
    #     r = len(s) - 1

    #     while l < r:
    #         if s[l] != s[r]:
    #             return False
    #         l += 1
    #         r -= 1

    #     return True

    # def isPalindrome(self, x: int) -> bool:
    #     if x < 0:
    #         return False
    #     elif x == 0:
    #         return True
    #     else:
    #         import math

    #         length = int(math.log(x, 10)) + 1

    #         while length > 1:
    #             l = x // 10 ** (length - 1)
    #             xr = x % 10 ** (length - 1)
    #             r = xr % 10

    #             if l != r:
    #                 return False

    #             length -= 2
    #             x = xr // 10

    #         return True

    # def isPalindrome(self, x: int) -> bool:
    #     if x < 0 or (x != 0 and x % 10 == 0):
    #         return False
    #     elif x == 0:
    #         return True
    #     else:
    #         import math

    #         length = int(math.log(x, 10)) + 1
    #         reverse_x = 0
    #         for i in range(length // 2):
    #             remainder = x % 10
    #             x = x // 10
    #             reverse_x = reverse_x * 10 + remainder
    #         if reverse_x == x or reverse_x == x // 10:
    #             return True
    #         else:
    #             return False

    # def isPalindrome(self, x: int) -> bool:
    #     if x < 0 or (x != 0 and x % 10 == 0):
    #         return False
    #     elif x == 0:
    #         return True
    #     else:
    #         reverse_x = 0
    #         while x > reverse_x:
    #             remainder = x % 10
    #             reverse_x = reverse_x * 10 + remainder
    #             x = x // 10
    #         if reverse_x == x or reverse_x // 10 == x:
    #             return True
    #         else:
    #             return False

    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


# @lc code=end
