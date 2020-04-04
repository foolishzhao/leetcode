class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0

        n, i = len(s), 1
        dp = [0] * (n + 1)
        while i < n:
            if s[i] == ')':
                j = i - dp[i] - 1
                if j >= 0 and s[j] == '(':
                    dp[i + 1] = dp[i] + dp[j] + 2

            i += 1

        return max(dp)
