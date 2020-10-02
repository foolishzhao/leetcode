class Solution:
    # time complexity: O(n*k*k), space complexity: O(n*k)
    # image put j into last pos, second to last pos, .., first pos
    # dp[i][j] = dp[i-1][j] + dp[i-1][j - 1] + ... + dp[i-1][j - i]
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[0] * (k + 1) for _ in range(n)]
        dp[0][0] = 1
        for i in range(1, n):
            dp[i][0] = 1
            for j in range(1, k + 1):
                dp[i][j] = sum(dp[i - 1][max(0, j - i):j + 1]) % mod

        return dp[-1][-1]

    # optimize space complexity to O(k)
    def kInversePairs2(self, n: int, k: int) -> int:
        mod = 10 ** 9 + 7
        dp = [0] * (k + 1)
        dp[0] = 1
        for i in range(1, n):
            for j in range(k, 0, -1):
                dp[j] = sum(dp[max(0, j - i):j + 1]) % mod

        return dp[-1]

    # optimize time complexity to O(n*k)
    # dp[i][j - 1] = dp[i-1][j - 1] + dp[i-1][j - 1] + ... + dp[i-1][j - i - 1]
    # dp[i][j] - dp[i][j - 1] = dp[i-1][j] - dp[i-1][j - i - 1]
    # dp[i][j] = dp[i][j - 1] + dp[i-1][j] - dp[i-1][j - i - 1]
    def kInversePairs3(self, n: int, k: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[0] * (k + 1) for _ in range(n)]
        dp[0][0] = 1
        for i in range(1, n):
            dp[i][0] = 1
            for j in range(1, k + 1):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
                if j - 1 >= i:
                    dp[i][j] -= dp[i - 1][j - 1 - i]
                dp[i][j] %= mod

        return dp[-1][-1]
