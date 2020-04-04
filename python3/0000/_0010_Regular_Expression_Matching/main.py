class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sLen, pLen = len(s), len(p)
        dp = [[False] * (pLen + 1) for _ in range(sLen + 1)]
        dp[0][0] = True

        for i in range(1, pLen):
            if p[i] == '*':
                dp[0][i + 1] = dp[0][i - 1]

        for i in range(sLen):
            for j in range(pLen):
                sc, pc = s[i], p[j]
                if sc == pc or pc == '.':
                    dp[i + 1][j + 1] = dp[i][j]
                elif pc == '*' and j > 0:
                    dp[i + 1][j + 1] = dp[i + 1][j - 1]
                    if sc == p[j - 1] or p[j - 1] == '.':
                        dp[i + 1][j + 1] = dp[i + 1][j + 1] or dp[i + 1][j] or dp[i][j + 1]

        return dp[sLen][pLen]


if __name__ == '__main__':
    Solution().isMatch("aa", "a")
