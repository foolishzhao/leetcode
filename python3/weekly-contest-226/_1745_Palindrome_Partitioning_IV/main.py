class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)

        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        for k in range(n):
            for i in range(n - k):
                j = i + k
                dp[i][j] = s[i] == s[j] and (dp[i + 1][j - 1] if i + 1 <= j - 1 else True)

        for j in range(n):
            for k in range(j + 1, n - 1):
                if dp[0][j] and dp[j + 1][k] and dp[k + 1][n - 1]:
                    return True
        return False
