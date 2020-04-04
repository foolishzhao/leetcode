import math


class Solution:
    def arrangeCoins(self, n: int) -> int:
        n <<= 1
        k = int(math.sqrt(n))
        while k * (k + 1) > n:
            k -= 1

        return k
