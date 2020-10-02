from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s, cur = sum(nums), 0
        for i, num in enumerate(nums):
            if s - num == 2 * cur:
                return i
            cur += num
        return -1
