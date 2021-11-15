from typing import List


class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        res, n = 0, len(nums)
        right = [0] * (n - 1) + [nums[-1]]
        for i in range(n - 2, -1, -1):
            right[i] = min(nums[i], right[i + 1])

        left = nums[0]
        for i in range(1, n - 1):
            if left < nums[i] < right[i + 1]:
                res += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                res += 1
            left = max(left, nums[i])
        return res
