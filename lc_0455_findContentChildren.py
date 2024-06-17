#
# @lc app=leetcode.cn id=455 lang=python3
#


# @lc code=start


from typing import Dict, List, Tuple


class Solution:
    # # 贪心
    # def findContentChildren(self, g: List[int], s: List[int]) -> int:
    #     g.sort()
    #     s.sort()

    #     j = 0
    #     for i in range(len(s)):
    #         if j == len(g):
    #             break
    #         if s[i] >= g[j]:
    #             j += 1

    #     return j

    # 动态规划
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(s) == 0:
            return 0

        g.sort()
        s.sort()

        lens = len(s)
        leng = len(g)
        dp: List[int] = [0 for _ in range(lens)]
        k = 0

        for i in range(lens):
            if k == leng and i >= k:
                dp[i] = dp[i - 1]
                continue
            x1 = 0 if i - 1 < 0 else dp[i - 1]
            if s[i] < g[k]:
                dp[i] = x1
            else:
                dp[i] = dp[i - 1] + 1
                k += 1

        return dp[lens - 1]

    # # 回溯
    # def findContentChildren(self, g: List[int], s: List[int]) -> int:
    #     lens = len(s)
    #     leng = len(g)
    #     lenmax = max(lens, leng)

    #     solutions: Dict[int, List[List[Tuple[int, int]]]] = dict()
    #     board: List[Tuple[int, int]] = []
    #     count = 0
    #     used: List[int] = []

    #     def backtrack(i):
    #         nonlocal count
    #         if i == lens:
    #             list = solutions.get(count) or []
    #             list.append(board.copy())
    #             solutions[count] = list
    #         else:
    #             for j in range(lenmax):
    #                 if j in used:
    #                     continue
    #                 used.append(j)
    #                 if j < leng:
    #                     board.append((i, j))
    #                     shouldIncrease = s[i] >= g[j]
    #                     if shouldIncrease:
    #                         count += 1
    #                 backtrack(i + 1)
    #                 used.pop()
    #                 if j < leng:
    #                     board.pop()
    #                     shouldIncrease = s[i] >= g[j]
    #                     if shouldIncrease:
    #                         count -= 1

    #     backtrack(0)

    #     for k, v in solutions.items():
    #         print(k)
    #         for item in v:
    #             print([(s[x[0]], g[x[1]]) for x in item])
    #     print()

    #     return max(list(solutions.keys()))


# @lc code=end
