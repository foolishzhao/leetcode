from typing import List


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        desc = False
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                if desc:
                    return False

                if i - 2 >= 0 and nums[i - 2] >= nums[i]:
                    nums[i] = nums[i - 1]

                desc = True

        return True
