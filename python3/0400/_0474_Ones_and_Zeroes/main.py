from typing import List


class Solution:
    # Time Limit Exceeded
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        if not strs:
            return 0
        k = len(strs)
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(k + 1)]
        for i in range(1, k + 1):
            s = strs[i - 1]
            zCount, oCount = s.count('0'), s.count('1')
            for u in range(m + 1):
                for v in range(n + 1):
                    dp[i][u][v] = dp[i - 1][u][v]
                    if u >= zCount and v >= oCount:
                        dp[i][u][v] = max(dp[i][u][v], dp[i - 1][u - zCount][v - oCount] + 1)

        return dp[-1][-1][-1]

    def findMaxForm2(self, strs: List[str], m: int, n: int) -> int:
        if not strs:
            return 0
        k = len(strs)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, k + 1):
            s = strs[i - 1]
            zCount, oCount = s.count('0'), s.count('1')
            for u in range(m, zCount - 1, -1):
                for v in range(n, oCount - 1, -1):
                    dp[u][v] = max(dp[u][v], dp[u - zCount][v - oCount] + 1)

        return dp[-1][-1]
