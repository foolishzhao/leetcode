from typing import List
import collections
import functools
import itertools


class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        n, sz = len(nums), len(nums) // k

        counter = collections.Counter(nums)
        if max(counter.values()) > k:
            return -1

        @functools.lru_cache(None)
        def dp(mask):
            if mask == 0:
                return 0

            res = float('inf')
            left = [i for i in range(n) if mask & (1 << i)]
            for comb in itertools.combinations(left, sz):
                elems = [nums[j] for j in comb]
                if len(set(elems)) != sz:
                    continue

                nextMask = mask
                for j in comb:
                    nextMask ^= 1 << j
                res = min(res, max(elems) - min(elems) + dp(nextMask))
            return res

        return dp((1 << n) - 1)
