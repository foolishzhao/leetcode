from typing import List


class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n, prefix = len(stones), [0] * len(stones)

        prefix[0] = stones[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + stones[i]

        dp = [0] * n
        dp[n - 2] = prefix[n - 1]
        for i in range(n - 3, -1, -1):
            dp[i] = max(dp[i + 1], prefix[i + 1] - dp[i + 1])
        return dp[0]

    def stoneGameVIII2(self, stones: List[int]) -> int:
        n = len(stones)

        for i in range(1, n):
            stones[i] += stones[i - 1]

        res = stones[n - 1]
        for i in range(n - 3, -1, -1):
            res = max(res, stones[i + 1] - res)
        return res
