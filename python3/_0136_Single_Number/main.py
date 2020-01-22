from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = 0
        for _, v in enumerate(nums):
            res ^= v

        return res
