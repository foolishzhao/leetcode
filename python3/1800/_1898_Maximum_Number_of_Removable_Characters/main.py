from typing import List


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def isSubseq(mi):
            bypass = set(removable[:mi + 1])
            i, j = 0, 0
            while i < len(s) and j < len(p):
                if i in bypass:
                    i += 1
                    continue

                if s[i] == p[j]:
                    j += 1

                i += 1
            return j == len(p)

        lo, hi = 0, len(removable) - 1
        while lo <= hi:
            mi = (hi - lo) // 2 + lo
            if isSubseq(mi):
                lo = mi + 1
            else:
                hi = mi - 1
        return lo
