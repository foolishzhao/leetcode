class Solution:
    # dp[n] = dp[n - 1] + dp[n - 2] + 2f(n - 1)
    # f(n - 1) = f(n - 2) + dp[n - 3]
    # dp[n] - dp[n - 1] = dp[n - 1] - dp[n - 3] + 2(f(n - 1) - f(n - 2)) -> dp[n] = 2dp[n - 1] + dp[n - 3]
    def numTilings(self, n: int) -> int:
        dp = [1, 2, 5] + [0] * n
        for i in range(3, n):
            dp[i] = 2 * dp[i - 1] + dp[i - 3]
        return dp[n - 1] % (10 ** 9 + 7)
