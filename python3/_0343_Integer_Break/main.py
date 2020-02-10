class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i // 2 + 1):
                dp[i] = max(dp[i], max(j, dp[j]) * max(i - j, dp[i - j]))

        return dp[-1]

    # If an optimal product contains a factor f >= 4, then you can replace it with factors 2 and f-2 without
    # losing optimality, as 2*(f-2) = 2f-4 >= f. So you never need a factor greater than or equal to 4,
    # meaning you only need factors 1, 2 and 3, and 1 is of course wasteful and you'd only need n=2 and n=3.
    #
    # 3*3 is simply better than 2*2*2, so you'd never use 2 more than twice.
    def integerBreak2(self, n: int) -> int:
        if n <= 3:
            return n - 1

        res = 1
        while n > 4:
            res *= 3
            n -= 3

        return res * n
