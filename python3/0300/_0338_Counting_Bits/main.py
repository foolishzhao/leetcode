from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        def numBits(n):
            cnt = 0
            while n:
                cnt += 1
                n &= (n - 1)
            return cnt

        return [numBits(x) for x in range(num + 1)]

    def countBits2(self, num: int) -> List[int]:
        dp = [0] * (num + 1)
        for i in range(1, num + 1):
            dp[i] = dp[i >> 1] + (i & 1)

        return dp
