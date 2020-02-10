from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patch, curMax, i = 0, 0, 0
        while curMax < n:
            if i < len(nums) and nums[i] <= curMax + 1:
                curMax += nums[i]
                i += 1
            else:
                patch += 1
                curMax += curMax + 1

        return patch
