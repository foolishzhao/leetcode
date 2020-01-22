from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        i, j, n = 0, 0, len(nums)
        while j < n:
            if nums[j]:
                nums[i] = nums[j]
                i += 1
            j += 1

        while i < n:
            nums[i] = 0
            i += 1
