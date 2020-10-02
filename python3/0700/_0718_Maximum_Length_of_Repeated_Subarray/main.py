from typing import List


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        m, n, res = len(A), len(B), 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                if A[i] == B[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                    res = max(res, dp[i + 1][j + 1])
        return res
