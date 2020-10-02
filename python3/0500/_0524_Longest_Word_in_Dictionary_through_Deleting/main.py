from typing import List


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort(key=lambda x: (-len(x), x))
        for x in d:
            if self.isSub(s, x):
                return x
        return ""

    def isSub(self, p, s):
        n, i = len(s), 0
        for c in p:
            if i < n and s[i] == c:
                i += 1
                if i == n:
                    return True
        return False
