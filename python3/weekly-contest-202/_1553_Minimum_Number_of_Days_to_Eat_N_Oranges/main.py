import functools


class Solution:
    # eat n % 2 oranges one-by-one and then swallow n / 2
    # eat n % 3 oranges one-by-one and then swallow n * 2 / 3
    @functools.lru_cache(None)
    def minDays(self, n: int) -> int:
        if n <= 1:
            return n

        return min(n % 2 + self.minDays(n >> 1) + 1, n % 3 + self.minDays(n // 3) + 1)
