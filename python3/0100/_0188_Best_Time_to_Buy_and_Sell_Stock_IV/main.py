from typing import List


class Solution:
    """
        dp[i, j] represents the max profit up until prices[j] using at most i transactions.
        dp[i, j] = max(dp[i, j-1], prices[j] - prices[jj] + dp[i-1, jj]) { jj in range of [0, j-1] }
                 = max(dp[i, j-1], prices[j] + max(dp[i-1, jj] - prices[jj]))
        dp[0, j] = 0; 0 transactions makes 0 profit
        dp[i, 0] = 0; if there is only one price data point you can't make any transaction.
    """

    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        if k >= n / 2:
            return sum(i - j for i, j in zip(prices[1:], prices[:-1]) if i > j)

        dp = [[0] * n for _ in range(k + 1)]
        for i in range(1, k + 1):
            t = -prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j - 1], prices[j] + t)
                t = max(t, dp[i - 1][j] - prices[j])

        return dp[-1][-1]
