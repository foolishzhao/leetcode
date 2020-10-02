class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:
        n = len(S)

        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1

        for k in range(1, n):
            for i in range(n - k):
                j = i + k
                if S[i] == S[j]:
                    lo, hi = i + 1, j - 1
                    while lo <= hi and S[lo] != S[j]:
                        lo += 1
                    while lo <= hi and S[hi] != S[j]:
                        hi -= 1

                    if lo > hi:
                        dp[i][j] = dp[i + 1][j - 1] * 2 + 2
                    elif lo == hi:
                        dp[i][j] = dp[i + 1][j - 1] * 2 + 1
                    else:
                        dp[i][j] = dp[i + 1][j - 1] * 2 - dp[lo + 1][hi - 1]
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]

        return dp[0][n - 1] % (10 ** 9 + 7)
