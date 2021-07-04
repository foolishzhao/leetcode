from typing import List
import collections


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n, prod = len(nums), collections.defaultdict(int)
        for i in range(n):
            for j in range(i + 1, n):
                prod[nums[i] * nums[j]] += 1
        return sum(v * (v - 1) * 4 for v in prod.values())
