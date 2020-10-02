from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()

        def count(d):
            res, cur = 1, position[0]
            for i in range(1, n):
                if position[i] - cur >= d:
                    res += 1
                    cur = position[i]
            return res

        lo, hi = 0, position[-1] - position[0]
        while lo < hi:
            # as we use lo = mi, prevent infinite loop
            mi = hi - (hi - lo) // 2
            if count(mi) < m:
                hi = mi - 1
            else:
                lo = mi
        return lo
