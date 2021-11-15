from typing import List


class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        dp = [0] * 3
        for num in nums:
            if num == 0:
                dp[0] += dp[0] + 1
            elif num == 1:
                dp[1] += dp[1] + dp[0]
            else:
                dp[2] += dp[2] + dp[1]
        return dp[2] % (10 ** 9 + 7)
