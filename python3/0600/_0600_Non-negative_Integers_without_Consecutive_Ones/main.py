class Solution:
    def findIntegers(self, num: int) -> int:
        # dp[i]: with i bits, number of non-negative integers whose binary representations without consecutive ones
        # dp[1] = 2, i.e. [0, 1]
        # dp[2] = 3, i.e. [00, 01, 10]
        dp = [0] * 32
        dp[0], dp[1] = 1, 2
        for i in range(2, 32):
            dp[i] = dp[i - 1] + dp[i - 2]

        res, preBit = 0, False
        for i in range(30, -1, -1):
            if num & (1 << i):
                # set this bit as 0, count number of ways for right i bits
                # then set this bit back to 1, count the remaining cases
                res += dp[i]
                if preBit:
                    return res
                preBit = True
            else:
                preBit = False

        # if not returned in line 15, then n is also a valid candidate
        return res + 1
