import functools
from typing import List


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        @functools.lru_cache(None)
        def helper(i, s):
            if i >= n:
                return 0

            ns = 1 - s
            if s == 1:
                curVal = stoneValue[i]
                dp[i][s] = curVal + helper(i + 1, ns)
                if i + 1 < n:
                    curVal += stoneValue[i + 1]
                    dp[i][s] = max(dp[i][s], curVal + helper(i + 2, ns))
                if i + 2 < n:
                    curVal += stoneValue[i + 2]
                    dp[i][s] = max(dp[i][s], curVal + helper(i + 3, ns))
            else:
                curVal = stoneValue[i]
                dp[i][s] = -curVal + helper(i + 1, ns)
                if i + 1 < n:
                    curVal += stoneValue[i + 1]
                    dp[i][s] = min(dp[i][s], -curVal + helper(i + 2, ns))
                if i + 2 < n:
                    curVal += stoneValue[i + 2]
                    dp[i][s] = min(dp[i][s], -curVal + helper(i + 3, ns))
            return dp[i][s]

        n = len(stoneValue)
        dp = [[float('-inf')] * 2 for _ in range(n)]
        helper(0, 1)

        if dp[0][1] > 0:
            return "Alice"
        elif dp[0][1] < 0:
            return "Bob"
        else:
            return "Tie"

    # dp[i]: max score Alice can get from stoneValue[i:]
    def stoneGameIII2(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [float('-inf')] * (n + 1)
        dp[n] = 0
        for i in range(n - 1, -1, -1):
            cur = stoneValue[i]
            dp[i] = cur - dp[i + 1]
            if i + 2 <= n:
                cur += stoneValue[i + 1]
                dp[i] = max(dp[i], cur - dp[i + 2])
            if i + 3 <= n:
                cur += stoneValue[i + 2]
                dp[i] = max(dp[i], cur - dp[i + 3])

        return "Alice" if dp[0] > 0 else "Bob" if dp[0] < 0 else "Tie"
