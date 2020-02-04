from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False

        m, n = s // 2, len(nums)
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True

        for i in range(1, n + 1):
            dp[i][0] = True
            for j in range(1, m + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= nums[i - 1]:
                    dp[i][j] |= dp[i - 1][j - nums[i - 1]]

        return dp[-1][-1]

    def canPartition2(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False

        m = s // 2
        dp = [True] + [False] * m
        for num in nums:
            for i in range(m, num - 1, -1):
                dp[i] |= dp[i - num]

        return dp[-1]
