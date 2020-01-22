class Solution:
    # Time limit exceeded
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(n):
            dp[i + 1] = dp[i] + 1
            j = 2
            while i + 1 - j ** 2 >= 0:
                dp[i + 1] = min(dp[i + 1], dp[i + 1 - j ** 2] + 1)
                j += 1

        return dp[-1]

    def numSquares2(self, n: int) -> int:
        l1, l2 = [0], []
        curLevel = 0

        visited = [False] * (n + 1)
        while True:
            curLevel += 1
            for v in l1:
                i = 1
                while True:
                    t = v + i ** 2
                    if t == n:
                        return curLevel
                    elif t > n:
                        break
                    else:
                        if not visited[t]:
                            l2.append(t)
                            visited[t] = True
                    i += 1

            l1, l2 = l2, []
