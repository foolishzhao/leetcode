from typing import List


class Solution:
    # target num separate nums into two part, in left part, nums[2 * m] == nums[2 * m + 1], m is the pair index
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) // 2
        while lo < hi:
            m = (hi - lo) // 2 + lo
            if nums[2 * m] == nums[2 * m + 1]:
                lo = m + 1
            else:
                hi = m
        return nums[2 * lo]
