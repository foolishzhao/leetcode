from typing import List


class Solution:
    # dp[i][j]: coins obtained from bursting all the balloons between index i and j (not including i or j)
    # If k is the index of the last balloon burst in (i, j)
    # dp[i][j] = max(nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j]) (k in (i+1,j))
    def maxCoins(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.insert(0, 1)
        nums.append(1)
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for k in range(2, n):
            for i in range(n - k):
                j = i + k
                for t in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], nums[i] * nums[t] * nums[j] + dp[i][t] + dp[t][j])

        return dp[0][-1]
