import functools


class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        # num of arrays for len i, largest num as j, k cost
        @functools.lru_cache(None)
        def dp(i, j, k):
            if not k:
                return 0

            if i == 1:
                return 1 if k == 1 else 0

            # add new num 1 to j to array end, and k keeps same
            res = dp(i - 1, j, k) * j
            # add new num j to array end, and k incr by 1
            res += sum(dp(i - 1, t, k - 1) for t in range(1, j))
            return res % mod

        mod = 10 ** 9 + 7
        return sum(dp(n, u, k) for u in range(1, m + 1)) % mod
