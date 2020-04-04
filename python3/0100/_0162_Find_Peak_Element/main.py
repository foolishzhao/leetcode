from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return -1

        n = len(nums)
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                return i

        return n - 1

    def findPeakElement2(self, nums: List[int]) -> int:
        if not nums:
            return -1

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (right - left) // 2 + left
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return left
