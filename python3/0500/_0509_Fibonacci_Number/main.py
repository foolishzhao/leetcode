import functools


class Solution:
    @functools.lru_cache(None)
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        return self.fib(N - 2) + self.fib(N - 1)
