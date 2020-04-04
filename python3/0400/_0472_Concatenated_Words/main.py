from typing import List


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        res = list()
        words.sort(key=lambda x: len(x))
        prefix = set()
        for w in words:
            # corner case: w must not be empty
            if w and self.dfs(prefix, w):
                res.append(w)
            prefix.add(w)

        return res

    def dfs(self, prefix, word):
        if not word:
            return True

        for i in range(len(word)):
            if word[:i + 1] in prefix and self.dfs(prefix, word[i + 1:]):
                return True

        return False


class Solution2:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        res = list()
        words.sort(key=lambda x: len(x))
        prefix = set()
        for w in words:
            if w and self.isValid(prefix, w):
                res.append(w)
            prefix.add(w)

        return res

    def isValid(self, prefix, word):
        n = len(word)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            for j in range(i + 1):
                if dp[j] and word[j: i + 1] in prefix:
                    dp[i + 1] = True
                    break
        return dp[-1]
