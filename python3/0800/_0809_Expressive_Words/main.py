from typing import List


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def isMatch(w):
            sLen, wLen, i, j = len(s), len(w), 0, 0
            prev = None
            while i < sLen and j < wLen:
                if s[i] != w[j]:
                    lo = i - 1
                    while lo >= 0 and s[lo] == prev:
                        lo -= 1

                    hi = i
                    while hi < sLen and s[hi] == prev:
                        hi += 1

                    if hi == sLen or hi - lo - 1 < 3 or s[hi] != w[j]:
                        return False

                    i = hi
                prev = s[i]
                i += 1
                j += 1
            return i == sLen and j == wLen

        s += '$'
        return sum([isMatch(w + '$') for w in words])

    def expressiveWords2(self, s: str, words: List[str]) -> int:
        def isMatch(w):
            sLen, wLen, j = len(s), len(w), 0
            for i in range(sLen):
                if j < wLen and s[i] == w[j]:
                    j += 1
                elif s[i - 2: i + 1] != s[i] * 3 != s[i - 1: i + 2]:
                    return False
            return j == wLen

        return sum([isMatch(w) for w in words])
