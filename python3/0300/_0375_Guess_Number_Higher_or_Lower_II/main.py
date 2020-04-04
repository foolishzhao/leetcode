class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        return self.helper(dp, 1, n)

    def helper(self, dp, i, j):
        if i >= j:
            return 0

        if dp[i][j] > 0:
            return dp[i][j]

        res = float('inf')
        for k in range(i, j + 1):
            res = min(res, k + max(self.helper(dp, i, k - 1), self.helper(dp, k + 1, j)))

        dp[i][j] = res
        return res
