from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0

        n = len(citations)
        lo, hi = 0, n - 1
        while lo <= hi:
            mi = (hi - lo) // 2 + lo
            if citations[mi] >= n - mi:
                if mi == lo or not (citations[mi - 1] >= n - mi + 1):
                    return n - mi
                hi = mi - 1
            else:
                lo = mi + 1
        return 0
