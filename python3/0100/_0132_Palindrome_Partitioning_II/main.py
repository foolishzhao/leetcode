class Solution:
    def minCut(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
            if i > 0 and s[i - 1] == s[i]:
                dp[i - 1][i] = True

        for k in range(2, n):
            for i in range(n - k):
                if dp[i + 1][i + k - 1] and s[i] == s[i + k]:
                    dp[i][i + k] = True

        cut = [0] * (n + 1)
        cut[0] = -1
        for i in range(n):
            cut[i + 1] = cut[i] + 1
            for j in range(i):
                if dp[j][i]:
                    cut[i + 1] = min(cut[i + 1], cut[j] + 1)

        return cut[-1]
