from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not g or not s:
            return 0

        g.sort()
        s.sort()
        res, i, j = 0, 0, 0
        while i < len(g):
            while j < len(s) and s[j] < g[i]:
                j += 1
            if j < len(s):
                res += 1
            i += 1
            j += 1

        return res

    def findContentChildren2(self, g: List[int], s: List[int]) -> int:
        if not g or not s:
            return 0

        g.sort()
        s.sort()
        res, i, j = 0, 0, 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                res += 1
                i += 1
            j += 1

        return res
