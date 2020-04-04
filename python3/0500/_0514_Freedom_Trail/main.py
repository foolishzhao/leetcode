import collections


class Solution:
    # dp[i][j] means if locates in i-index in key, j-index in ring, minimum steps to achieve key
    def findRotateSteps(self, ring: str, key: str) -> int:
        n, m = len(ring), len(key)
        dp = [[0] * n for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n):
                dp[i][j] = float('inf')
                for k in range(n):
                    if ring[k] == key[i]:
                        step = abs(j - k)
                        step = min(step, n - step)
                        dp[i][j] = min(dp[i][j], step + dp[i + 1][k])
        return dp[0][0] + m

    def findRotateSteps2(self, ring: str, key: str) -> int:
        dt = collections.defaultdict(list)
        for i, c in enumerate(ring):
            dt[c].append(i)

        n, m = len(ring), len(key)
        dp = [[0] * n for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n):
                dp[i][j] = float('inf')
                for k in dt[key[i]]:
                    step = abs(j - k)
                    step = min(step, n - step)
                    dp[i][j] = min(dp[i][j], step + dp[i + 1][k])
        return dp[0][0] + m

    # forward dp
    def findRotateSteps3(self, ring: str, key: str) -> int:
        dt = collections.defaultdict(list)
        for i, c in enumerate(ring):
            dt[c].append(i)

        n, m = len(ring), len(key)
        # pos: min steps
        cur = {0: 0}
        for c in key:
            nxt = {}
            for i in dt[c]:
                nxt[i] = float('inf')
                for j in cur:
                    step = abs(i - j)
                    step = min(step, n - step)
                    nxt[i] = min(nxt[i], step + cur[j])
            cur = nxt
        return min(cur.values()) + m
