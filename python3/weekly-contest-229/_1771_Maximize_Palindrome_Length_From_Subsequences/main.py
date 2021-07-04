class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        m, n, t, res, w = len(word1), len(word2), len(word1) + len(word2), 0, word1 + word2
        dp = [[0] * t for _ in range(t)]
        for k in range(t):
            for i in range(t - k):
                j = i + k
                if k == 0:
                    dp[i][j] = 1
                else:
                    if w[i] == w[j]:
                        dp[i][j] = dp[i + 1][j - 1] + 2
                        if i < m <= j:
                            res = max(res, dp[i][j])
                    else:
                        dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return res
