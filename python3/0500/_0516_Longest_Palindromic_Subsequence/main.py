class Solution:
    # dp[i][j]: the longest palindromic subsequence's length of substring(i, j)
    # if s.charAt(i) == s.charAt(j) dp[i][j] = dp[i+1][j-1] + 2
    # otherwise, dp[i][j] = Math.max(dp[i+1][j], dp[i][j-1])
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        dp = [[0] * n for _ in range(n)]
        # more elegant than first init k = 1, 2, than for loop for k in (3, n)
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]
