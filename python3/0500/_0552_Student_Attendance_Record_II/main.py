class Solution:
    # only consider 'P' and 'L'
    # dp[i][0] how many records end with 'P' with length i
    # dp[i][1] how many records end with 'PL' with length i
    # dp[i][2] how many records end with 'LL' with length i
    def checkRecord(self, n: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[0] * 3 for _ in range(n + 1)]
        dp[0] = [1, 0, 0]
        dp[1] = [1, 1, 0]
        for i in range(2, n + 1):
            dp[i][0] = sum(dp[i - 1]) % mod
            dp[i][1] = dp[i - 1][0]
            dp[i][2] = dp[i - 1][1]

        # zero 'A'
        res = sum(dp[n]) % mod
        for i in range(n):
            # one 'A' at position 0 ~ n - 1
            res += sum(dp[i]) * sum(dp[n - 1 - i])
            res %= mod

        return res
