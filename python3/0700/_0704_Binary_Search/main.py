from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mi = (hi - lo) // 2 + lo
            if nums[mi] == target:
                return mi
            elif nums[mi] > target:
                hi = mi - 1
            else:
                lo = mi + 1
        return -1
