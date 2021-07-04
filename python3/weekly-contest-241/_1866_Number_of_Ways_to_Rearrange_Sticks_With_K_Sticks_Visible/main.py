import functools


class Solution:

    def rearrangeSticks(self, n: int, k: int) -> int:
        @functools.lru_cache(None)
        def A(x):
            res = 1
            for i in range(1, x + 1):
                res *= i
            return res

        @functools.lru_cache(None)
        def dfs(n, k):
            if k == 0 or n < k:
                return 0

            if n == k:
                return 1

            if k == 1:
                return A(n - 1) % (10 ** 9 + 7)

            return ((n - 1) * dfs(n - 1, k) + dfs(n - 1, k - 1)) % (10 ** 9 + 7)

        return dfs(n, k)
