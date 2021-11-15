from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = sorted([num for row in grid for num in row])
        for prev, cur in zip(nums, nums[1:]):
            if (cur - prev) % x != 0:
                return -1

        mid = nums[len(nums) // 2]
        return sum([abs(num - mid) // x for num in nums])
