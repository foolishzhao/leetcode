from typing import List

import functools


class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        @functools.lru_cache(None)
        def dp(i, j):
            if i < j:
                return float('-inf')

            if j == 1:
                return sum(nums[:i]) / i

            res = float('-inf')
            for t in range(1, i + 1):
                res = max(res, dp(i - t, j - 1) + sum(nums[i - t:i]) / t)
            return res

        return dp(len(nums), k)
