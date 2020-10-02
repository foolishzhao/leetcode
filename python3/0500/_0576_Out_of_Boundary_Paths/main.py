import functools


class Solution:
    # bfs, time complexity: O(4 ^ N)
    # Time Limit Exceeded
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        q = [(i, j, N)]
        res = 0
        while q:
            i, j, N = q.pop(0)
            if i < 0 or i >= m or j < 0 or j >= n:
                res += 1
            elif N > 0:
                q.append((i - 1, j, N - 1))
                q.append((i, j - 1, N - 1))
                q.append((i + 1, j, N - 1))
                q.append((i, j + 1, N - 1))
        return res

    # memorized dp, time complexity: O(m * n * N)
    def findPaths2(self, m: int, n: int, N: int, i: int, j: int) -> int:
        @functools.lru_cache(None)
        def dp(x, y, t):
            if not (0 <= x < m and 0 <= y < n):
                return 1

            if t == 0:
                return 0

            return dp(x - 1, y, t - 1) + dp(x + 1, y, t - 1) + dp(x, y - 1, t - 1) + dp(x, y + 1, t - 1)

        return dp(i, j, N) % (10 ** 9 + 7)

    # dp[k][u][v] stands for how many possible ways to walk into cell u,v in step t.
    # dp[k][u][v] only depends on dp[k - 1][u][v], so can compress 3 dimensional dp to 2 dimensional.
    def findPaths3(self, m: int, n: int, N: int, i: int, j: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[i][j] = 1

        res, mod = 0, 10 ** 9 + 7
        for _ in range(N):
            nxt = [[0] * n for _ in range(m)]
            for u in range(m):
                for v in range(n):
                    for du, dv in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                        nu, nv = u + du, v + dv
                        if 0 <= nu < m and 0 <= nv < n:
                            nxt[nu][nv] = (nxt[nu][nv] + dp[u][v]) % mod
                        else:
                            res = (res + dp[u][v]) % mod
            dp = nxt

        return res
