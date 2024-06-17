#
# @lc app=leetcode.cn id=62 lang=python3
#


# @lc code=start


from typing import List, Tuple


class Solution:
    # # 回溯
    # def uniquePaths(self, m: int, n: int) -> int:
    #     solutions: List[List[Tuple[int, int]]] = []
    #     board: List[Tuple[int, int]] = []

    #     def backtrack(p: Tuple[int, int]):
    #         board.append(p)

    #         if p[0] == m - 1 and p[1] == n - 1:
    #             solutions.append(board.copy())
    #         else:
    #             if p[1] + 1 < n:
    #                 backtrack((p[0], p[1] + 1))

    #             if p[0] + 1 < m:
    #                 backtrack((p[0] + 1, p[1]))

    #         board.pop()

    #     backtrack((0, 0))

    #     # print(f"{m}, {n}: ")
    #     # for i, item in enumerate(solutions):
    #     #     print(f"{i}: ")
    #     #     print(item)
    #     # print()

    #     return len(solutions)

    # 动规
    def uniquePaths(self, m: int, n: int) -> int:
        dp: List[List[int]] = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = dp[i][j - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        return dp[m - 1][n - 1]


# @lc code=end
