from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return 0

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (right - left) // 2 + left
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
