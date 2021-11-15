from typing import List


class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        n = len(nextVisit)
        dp = [0] * n
        for i in range(1, n):
            # - dp[nextVisit[i - 1]]: can think it as 1st time to arrive at nextVisit[i - 1]
            dp[i] = 2 * dp[i - 1] - dp[nextVisit[i - 1]] + 2

        return dp[-1] % (10 ** 9 + 7)
