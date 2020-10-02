class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(1, n):
            prev, cur = s[i - 1], s[i]
            if cur > '0':
                dp[i + 1] = dp[i]

            if prev == '1':
                dp[i + 1] += dp[i - 1]
            elif prev == '2':
                if cur <= '6':
                    dp[i + 1] += dp[i - 1]

        return dp[-1]