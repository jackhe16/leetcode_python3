#
# @lc app=leetcode.cn id=0 lang=python3
#


# @lc code=start


from typing import List


class Solution:
    def __init__(self) -> None:
        self.x = 0

    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        self.move(len(A), A, B, C)
        print(self.x)

    def move(self, n: int, A: List[int], B: List[int], C: List[int]):
        if n == 1:
            C.append(A.pop())
            print(f"{A} -> {C}")
            self.x += 1
        else:
            self.move(n - 1, A, C, B)
            C.append(A.pop())
            print(f"{A} -> {C}")
            self.x += 1
            self.move(n - 1, B, A, C)


# @lc code=end
