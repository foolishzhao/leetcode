class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)

        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]

        dp[0][0] = 0
        for i in range(m):
            dp[i + 1][0] = dp[i][0] + ord(s1[i])
        for i in range(n):
            dp[0][i + 1] = dp[0][i] + ord(s2[i])

        for i in range(m):
            for j in range(n):
                if s1[i] == s2[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = min(dp[i + 1][j] + ord(s2[j]), dp[i][j + 1] + ord(s1[i]))

        return dp[m][n]

    def minimumDeleteSum2(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)

        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for j in range(n):
            dp[j + 1] = dp[j] + ord(s2[j])

        for i in range(m):
            t1 = dp[0]
            dp[0] += ord(s1[i])
            for j in range(n):
                t2 = dp[j + 1]
                if s1[i] == s2[j]:
                    dp[j + 1] = t1
                else:
                    dp[j + 1] = min(dp[j] + ord(s2[j]), dp[j + 1] + ord(s1[i]))
                t1 = t2
        return dp[n]
