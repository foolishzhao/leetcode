from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        cIndexes = [float('-inf')]
        for i, x in enumerate(s):
            if x == c:
                cIndexes.append(i)
        cIndexes.append(float('inf'))

        res, j = list(), 1
        for i in range(len(s)):
            res.append(min(abs(cIndexes[j - 1] - i), abs(cIndexes[j] - i)))
            if i == cIndexes[j]:
                j += 1
        return res

    def shortestToChar2(self, s: str, c: str) -> List[int]:
        n, pos = len(s), float('-inf')

        res = [n] * n
        for i in range(n):
            if s[i] == c:
                pos = i
            res[i] = min(res[i], abs(pos - i))

        for i in reversed(range(n)):
            if s[i] == c:
                pos = i
            res[i] = min(res[i], abs(pos - i))
        return res
