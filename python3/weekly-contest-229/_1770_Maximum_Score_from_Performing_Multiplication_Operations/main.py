import functools
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)

        @functools.lru_cache(1000)
        def dp(i, j):
            idx = i + n - 1 - j
            if idx >= m:
                return 0
            return max(multipliers[idx] * nums[i] + dp(i + 1, j), multipliers[idx] * nums[j] + dp(i, j - 1))

        return dp(0, n - 1)

    # dp[i][j] represents pick i elements from left and pick j elements from right of nums
    def maximumScore2(self, nums: List[int], multipliers: List[int]) -> int:
        m, n, res = len(multipliers), len(nums), float('-inf')
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(m - i + 1):
                if not i and not j:
                    continue

                l, r = float('-inf'), float('-inf')
                if i:  # pick left
                    l = dp[i - 1][j] + multipliers[i + j - 1] * nums[i - 1]
                if j:  # pick right
                    r = dp[i][j - 1] + multipliers[i + j - 1] * nums[n - j]
                dp[i][j] = max(l, r)
                if i + j == m:
                    res = max(res, dp[i][j])
        return res
