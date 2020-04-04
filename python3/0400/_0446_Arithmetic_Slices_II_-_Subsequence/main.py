from typing import List
import collections


class Solution:
    # dp[i][diff]: number of slices end with i at diff diff, at least length 2
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        n, res = len(A), 0
        dp = [collections.defaultdict(int) for _ in range(n)]

        for i in range(n):
            for j in range(i):
                diff = A[i] - A[j]
                dp[i][diff] += dp[j][diff] + 1
                res += dp[j][diff]

        return res
