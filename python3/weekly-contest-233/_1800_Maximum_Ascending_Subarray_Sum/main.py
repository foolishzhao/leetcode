from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        nums.append(0)

        res, cur = 0, nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                res = max(res, cur)
                cur = 0
            cur += nums[i]
        return res
