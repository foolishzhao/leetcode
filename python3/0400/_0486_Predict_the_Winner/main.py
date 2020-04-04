from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[[-1, -1] for _ in range(n)] for _ in range(n)]
        self.helper(nums, dp, 0, n - 1, 1)
        return dp[0][n - 1][1] >= 0

    def helper(self, nums, dp, i, j, s):
        if i > j:
            return 0

        if dp[i][j][s] != -1:
            return dp[i][j][s]

        ns = 1 - s
        if s == 1:
            dp[i][j][s] = max(nums[i] + self.helper(nums, dp, i + 1, j, ns),
                              nums[j] + self.helper(nums, dp, i, j - 1, ns))
        else:
            dp[i][j][s] = min(-nums[i] + self.helper(nums, dp, i + 1, j, ns),
                              -nums[j] + self.helper(nums, dp, i, j - 1, ns))

        return dp[i][j][s]

    def PredictTheWinner2(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = nums[i]

        for k in range(1, n):
            for i in range(n - k):
                j = i + k
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])

        return dp[0][n - 1] >= 0

    def PredictTheWinner3(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [0] * n

        for i in range(n - 1, -1, -1):
            dp[i] = nums[i]
            for j in range(i + 1, n):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])

        return dp[-1] >= 0
