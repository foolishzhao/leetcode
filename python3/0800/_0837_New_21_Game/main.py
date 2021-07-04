class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts - 1:
            return 1

        dp, ps = [1] + [0] * n, 1
        for i in range(1, n + 1):
            dp[i] = ps / maxPts
            if i < k:
                ps += dp[i]
            if i >= maxPts:
                ps -= dp[i - maxPts]
        return sum(dp[k:])
