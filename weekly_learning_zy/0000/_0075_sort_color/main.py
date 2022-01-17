from _ast import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1

        for i in range(r + 1):
            while nums[i] == 2 and i < r:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            while nums[i] == 0 and i > l:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1



