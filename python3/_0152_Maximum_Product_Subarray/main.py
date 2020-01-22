from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        curMin, curMax, n, res = nums[0], nums[0], len(nums), nums[0]
        for i in range(1, n):
            prevMax = curMax
            curMax = max(nums[i], prevMax * nums[i], curMin * nums[i])
            curMin = min(nums[i], prevMax * nums[i], curMin * nums[i])
            res = max(res, curMax)

        return res
