from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if not dungeon or not dungeon[0]:
            return 0

        m, n = len(dungeon), len(dungeon[0])

        dp = [[0] * n for _ in range(m)]
        dp[-1][-1] = max(-dungeon[-1][-1] + 1, 1)

        for i in range(m - 2, -1, -1):
            dp[i][n - 1] = max(dp[i + 1][n - 1] - dungeon[i][n - 1], 1)

        for i in range(n - 2, -1, -1):
            dp[m - 1][i] = max(dp[m - 1][i + 1] - dungeon[m - 1][i], 1)

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = max(min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j], 1)

        return dp[0][0]
