from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        for i in range(n):
            if nums[i] >= n - i:
                if i == 0 or nums[i - 1] < n - i:
                    return n - i
        return -1
