from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        if not words:
            return 0

        wordBits = [self.getWordBit(w) for w in words]
        res, n = 0, len(words)
        for i in range(n):
            for j in range(i + 1, n):
                if not (wordBits[i] & wordBits[j]):
                    res = max(res, len(words[i]) * len(words[j]))

        return res

    def getWordBit(self, w):
        res = 0
        for c in w:
            b = ord(c) - ord('a')
            res |= (1 << b)

        return res
