from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 1, len(nums) - 1
        while left < right:
            mid = (right - left) // 2 + left
            cnt = sum([1 if x <= mid else 0 for x in nums])
            if cnt <= mid:
                left = mid + 1
            else:
                right = mid

        return left

    def findDuplicate2(self, nums: List[int]) -> int:
        if not nums:
            return -1

        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
