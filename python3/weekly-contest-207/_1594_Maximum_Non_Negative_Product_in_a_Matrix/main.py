from typing import List


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[0] * 2 for _ in range(n)] for _ in range(m)]
        dp[0][0] = [grid[0][0]] * 2
        for i in range(1, m):
            dp[i][0] = [dp[i - 1][0][0] * grid[i][0], dp[i - 1][0][1] * grid[i][0]]
        for j in range(1, n):
            dp[0][j] = [dp[0][j - 1][0] * grid[0][j], dp[0][j - 1][1] * grid[0][j]]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j][1] = max(
                    grid[i][j] * dp[i - 1][j][0],
                    grid[i][j] * dp[i - 1][j][1],
                    grid[i][j] * dp[i][j - 1][0],
                    grid[i][j] * dp[i][j - 1][1],
                )

                dp[i][j][0] = min(
                    grid[i][j] * dp[i - 1][j][0],
                    grid[i][j] * dp[i - 1][j][1],
                    grid[i][j] * dp[i][j - 1][0],
                    grid[i][j] * dp[i][j - 1][1],
                )

        return dp[-1][-1][1] % (10 ** 9 + 7) if dp[-1][-1][1] >= 0 else -1
