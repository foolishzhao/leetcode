import functools


class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        dirs = [[1, 2], [1, -2], [-1, -2], [-1, 2], [2, 1], [2, -1], [-2, -1], [-2, 1]]

        @functools.lru_cache(None)
        def prob(i, j, k):
            if i < 0 or i >= N or j < 0 or j >= N:
                return 0

            if k == 0:
                return 1

            res = 0
            for di, dj in dirs:
                res += prob(i + di, j + dj, k - 1) / 8
            return res

        return prob(r, c, K)
