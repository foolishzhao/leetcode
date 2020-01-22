from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s or not wordDict:
            return False

        n = len(s)
        dp = [False] * (n + 1)

        dp[0] = True
        for i in range(n):
            for word in wordDict:
                j = i - len(word) + 1
                if j >= 0 and dp[j] and s[j:i + 1] == word:
                    dp[i + 1] = True
                    break

        return dp[-1]
