class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] != '0':
            return False

        n = len(s)
        dp = [True] + [False] * (n - 1)

        lo, hi, cnt = 1 - maxJump, 1 - minJump, 0
        for i in range(lo, hi + 1):
            if i >= 0 and dp[i]:
                cnt += 1

        for i in range(1, n):
            dp[i] = s[i] == '0' and cnt > 0

            cnt -= lo >= 0 and dp[lo]
            lo += 1
            hi += 1
            cnt += hi >= 0 and dp[hi]

        return dp[-1]

    def canReach2(self, s: str, minJump: int, maxJump: int) -> bool:
        n, cnt = len(s), 0
        dp = [True] + [False] * (n - 1)
        for i in range(1, n):
            if i > maxJump:
                cnt -= dp[i - maxJump - 1]
            if i >= minJump:
                cnt += dp[i - minJump]
            dp[i] = s[i] == '0' and cnt > 0
        return dp[-1]
