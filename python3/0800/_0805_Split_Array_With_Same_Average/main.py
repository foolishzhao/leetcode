from typing import List
import functools


class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        @functools.lru_cache(None)
        def find(target, k, i):
            if k == 0:
                return target == 0

            if target < 0 or i + k > n:
                return False

            return find(target - nums[i], k - 1, i + 1) or find(target, k, i + 1)

        s, n = sum(nums), len(nums)
        for k in range(1, n // 2 + 1):
            if s * k % n == 0 and find(s * k // n, k, 0):
                return True
        return False
