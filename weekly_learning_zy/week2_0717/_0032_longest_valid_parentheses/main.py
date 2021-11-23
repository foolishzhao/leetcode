class Solution:
    def longestValidParentheses(self, s: str) -> int:

        if not s:
            return 0

        n = len(s)
        dp = [0] * n
        for i in range(n - 2, -1, -1):
            if s[i] == '(':
                j = i + dp[i + 1] + 1
                if j < n and s[j] == ')':
                    dp[i] = dp[i + 1] + 2
                    if j + 1 < n:
                        dp[i] += dp[j + 1]
        return max(dp)