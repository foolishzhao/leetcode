from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        return self.helper(rating) + self.helper(rating[::-1])

    def helper(self, rating):
        res, n = 0, len(rating)
        dp = [0] * n
        for i in range(1, n):
            for j in range(i):
                if rating[i] > rating[j]:
                    dp[i] += 1

        for i in range(1, n):
            for j in range(i):
                if rating[i] > rating[j]:
                    res += dp[j]

        return res
