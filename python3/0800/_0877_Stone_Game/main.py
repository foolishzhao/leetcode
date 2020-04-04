from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[[-1] * 2 for _ in range(n)] for _ in range(n)]
        self.helper(dp, piles, 0, n - 1, 1)

        return dp[0][n - 1][1] > 0

    def helper(self, dp, piles, i, j, s):
        if i > j:
            return 0

        if dp[i][j][s] != -1:
            return dp[i][j][s]

        ns = 1 - s
        if s == 1:
            dp[i][j][s] = max(piles[i] + self.helper(dp, piles, i + 1, j, ns),
                              piles[j] + self.helper(dp, piles, i, j - 1, ns))
        else:
            dp[i][j][s] = min(-piles[i] + self.helper(dp, piles, i + 1, j, ns),
                              -piles[j] + self.helper(dp, piles, i, j - 1, ns))

        return dp[i][j][s]
