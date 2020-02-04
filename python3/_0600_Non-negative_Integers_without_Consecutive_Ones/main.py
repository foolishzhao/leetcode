class Solution:
    def findIntegers(self, num: int) -> int:
        dp = [0] * 32
        dp[0] = 1
        dp[1] = 2
        for i in range(2, 32):
            dp[i] = dp[i - 1] + dp[i - 2]

        res, preBit = 0, False
        for i in range(30, -1, -1):
            if num & (1 << i):
                res += dp[i]
                if preBit:
                    return res
                preBit = True
            else:
                preBit = False

        return res + 1
