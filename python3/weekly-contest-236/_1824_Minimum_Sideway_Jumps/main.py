from typing import List


class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        dp = [[float('inf')] * 3 for _ in range(n)]
        dp[0] = [1, 0, 1]
        for i in range(1, n):
            for j in range(3):
                if obstacles[i] != j + 1:
                    dp[i][j] = dp[i - 1][j]
            curMin = min(dp[i])
            for j in range(3):
                if obstacles[i] != j + 1:
                    dp[i][j] = curMin if dp[i][j] == curMin else curMin + 1
        return min(dp[n - 1])
