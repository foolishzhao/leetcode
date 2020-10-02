class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        n = len(s)
        dp = [1] + [0] * n
        dp[1] = 9 if s[0] == '*' else 1
        for i in range(1, n):
            prev, cur = s[i - 1], s[i]
            if cur == '*':
                dp[i + 1] = 9 * dp[i]
            elif cur > '0':
                dp[i + 1] = dp[i]

            if prev == '*':
                if cur == '*':
                    dp[i + 1] += 15 * dp[i - 1]
                elif cur <= '6':
                    dp[i + 1] += 2 * dp[i - 1]
                else:
                    dp[i + 1] += dp[i - 1]
            elif prev == '1':
                if cur == '*':
                    dp[i + 1] += 9 * dp[i - 1]
                else:
                    dp[i + 1] += dp[i - 1]
            elif prev == '2':
                if cur == '*':
                    dp[i + 1] += 6 * dp[i - 1]
                elif cur <= '6':
                    dp[i + 1] += dp[i - 1]
            dp[i + 1] %= 10 ** 9 + 7

        return dp[-1]

