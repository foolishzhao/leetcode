import functools
from typing import List


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        @functools.lru_cache(None)
        def dp(u, v, w):
            if apple[u][v] < w:
                return 0

            if w == 1:
                return 1

            nu, nv = u + 1, v + 1
            while nu < m and apple[u][v] == apple[nu][v]:
                nu += 1
            while nv < n and apple[u][v] == apple[u][nv]:
                nv += 1

            res = 0
            while nu < m:
                res += dp(nu, v, w - 1)
                nu += 1
            while nv < n:
                res += dp(u, nv, w - 1)
                nv += 1
            return res

        m, n = len(pizza), len(pizza[0])
        apple = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                apple[i][j] = pizza[i][j] == 'A'
                apple[i][j] += apple[i + 1][j] + apple[i][j + 1] - apple[i + 1][j + 1]

        return dp(0, 0, k) % (10 ** 9 + 7)
