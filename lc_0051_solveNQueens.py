#
# @lc app=leetcode.cn id=51 lang=python3
#


# @lc code=start


class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        def generateBoard():
            board = list()
            for i in range(n):
                row[queens[i]] = "Q"
                board.append("".join(row))
                row[queens[i]] = "."
            return board

        def backtrack(row: int):
            if row == n:
                solutions.append(generateBoard())
            else:
                for i in range(n):
                    if i in columns or row - i in diagonal1 or row + i in diagonal2:
                        continue
                    queens[row] = i
                    columns.add(i)
                    diagonal1.add(row - i)
                    diagonal2.add(row + i)
                    backtrack(row + 1)
                    columns.remove(i)
                    diagonal1.remove(row - i)
                    diagonal2.remove(row + i)

        solutions: list[list[str]] = list()
        queens = [-1] * n
        columns: set[int] = set()
        diagonal1: set[int] = set()
        diagonal2: set[int] = set()
        row = ["."] * n
        backtrack(0)
        return solutions


# @lc code=end
