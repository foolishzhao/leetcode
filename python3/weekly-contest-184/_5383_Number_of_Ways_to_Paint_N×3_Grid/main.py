class Solution:
    # with i * 3 grid
    # dp[i][0] denotes num of ways for pattern aba in last row
    # dp[i][1] denotes num of ways for pattern abc in last row
    # dp[i] only rely on dp[i-1]
    def numOfWays(self, n: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[0] * 2 for _ in range(n)]
        dp[0] = [6, 6]
        for i in range(1, n):
            dp[i][0] = (dp[i - 1][0] * 3 + dp[i - 1][1] * 2) % mod
            dp[i][1] = (dp[i - 1][0] * 2 + dp[i - 1][1] * 2) % mod

        return sum(dp[-1]) % mod

    # optimize space
    def numOfWays2(self, n: int) -> int:
        aba, abc, mod = 6, 6, 10 ** 9 + 7
        for i in range(1, n):
            aba, abc = aba * 3 + abc * 2, aba * 2 + abc * 2
        return (aba + abc) % mod
