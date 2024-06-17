class Solution:
    def bag(self, size: int, weights: list[int], values: list[int]):
        rows, cols = len(weights), size + 1
        dp: list[list[int]] = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if i == 0:
                    dp[i][j] = 0 if j - weights[i] < 0 else values[i]
                else:
                    x1 = 0 if j == 0 else dp[i - 1][j]
                    x2 = 0 if j - weights[i] < 0 else dp[i - 1][j - weights[i]] + values[i]
                    dp[i][j] = max(x1, x2)

        print("bag ", size, weights, values)
        for x in dp:
            print(x)
        print()

        return dp[rows - 1][cols - 1]
