class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        dp = [True] * n
        res = 0
        for i in range(2, n):
            if dp[i]:
                res += 1
                j = i
                while i * j < n:
                    dp[i * j] = False
                    j += 1

        return res
