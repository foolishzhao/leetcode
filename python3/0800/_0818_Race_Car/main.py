import functools


class Solution:
    def racecar(self, target: int) -> int:
        @functools.lru_cache(None)
        def dp(i):
            if i == 0:
                return 0

            n = i.bit_length()
            if 2 ** n - 1 == i:
                return n

            res = dp(2 ** n - 1 - i) + n + 1
            for m in range(0, n - 1):
                res = min(res, dp(i - 2 ** (n - 1) + 2 ** m) + n + m + 1)
            return res

        return dp(target)
