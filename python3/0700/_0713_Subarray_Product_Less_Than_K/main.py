from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res, i, cur = 0, 0, 1
        for j in range(len(nums)):
            cur *= nums[j]
            while cur >= k and i <= j:
                cur /= nums[i]
                i += 1
            res += j - i + 1
        return res
