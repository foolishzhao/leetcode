from typing import List
import collections


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        res, i = 0, 0
        for j, num in enumerate(nums):
            while num - nums[i] > 1:
                i += 1
            if num > nums[i]:
                res = max(res, j - i + 1)
        return res

    def findLHS2(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        res = 0
        for k, v in counter.items():
            if k - 1 in counter:
                res = max(res, v + counter[k - 1])
        return res
