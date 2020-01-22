from typing import List


class Solution:
    # convert problem to non-cycle sub-problems
    # case 1: not stole 1, n
    # case 2: stole 1, not n
    # case 3: stole n, not 1
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        return max(self.robHelper(nums[:-1]), self.robHelper(nums[1:]))

    def robHelper(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        one, two, three = 0, 0, 0
        for i in range(0, n):
            three = max(nums[i] + one, two)
            one, two = two, three

        return three
