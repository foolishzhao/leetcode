from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        idx, mx = -1, max(nums)
        for i, num in enumerate(nums):
            if num == mx:
                idx = i
            elif mx < 2 * num:
                return -1
        return idx
