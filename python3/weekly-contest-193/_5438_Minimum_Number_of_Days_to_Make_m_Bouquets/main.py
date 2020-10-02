from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n:
            return -1

        def getBouquet(midDay):
            res, i = 0, 0
            for j, d in enumerate(bloomDay + [float('inf')]):
                if d > midDay:
                    if j and bloomDay[j - 1] <= midDay:
                        res += (j - 1 - i + 1) // k
                else:
                    if j and bloomDay[j - 1] > midDay:
                        i = j
            return res

        day = sorted(list(set(bloomDay)))
        lo, hi = 0, len(day) - 1
        while lo < hi:
            mi = (hi - lo) // 2 + lo
            if getBouquet(day[mi]) < m:
                lo = mi + 1
            else:
                hi = mi
        return day[lo]
