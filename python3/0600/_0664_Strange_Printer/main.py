class Solution:
    def strangePrinter(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        dp = [[n] * n for _ in range(n)]
        for k in range(n):
            for i in range(n - k):
                j = i + k
                if j == i:
                    dp[i][j] = 1
                else:
                    for t in range(i, j):
                        dp[i][j] = min(dp[i][j], dp[i][t] + dp[t + 1][j])

                    if s[i] == s[j]:
                        dp[i][j] -= 1
        return dp[0][n - 1]
