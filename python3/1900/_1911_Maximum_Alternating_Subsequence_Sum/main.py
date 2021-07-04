from typing import List


class Solution:
    # dp1[i] max alternating sum util index i, the last element we taken was with negative sign
    # dp2[i] max alternating sum util index i, the last element we taken was with positive sign
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        dp1, dp2 = [0] * (n + 1), [0] * (n + 1)
        for i in range(n):
            dp1[i + 1] = max(dp1[i], dp2[i] - nums[i])
            dp2[i + 1] = max(dp2[i], dp1[i] + nums[i])

        return max(dp1[-1], dp2[-1])
