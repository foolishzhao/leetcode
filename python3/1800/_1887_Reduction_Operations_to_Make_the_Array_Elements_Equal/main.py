from typing import List
import collections


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        dt = collections.defaultdict(int)
        for num in nums:
            dt[num] += 1

        order = sorted(dt.keys())
        return sum([dt[o] * i for i, o in enumerate(order)])

    def reductionOperations2(self, nums: List[int]) -> int:
        nums.sort()

        res, order = 0, 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                order += 1
            res += order
        return res
