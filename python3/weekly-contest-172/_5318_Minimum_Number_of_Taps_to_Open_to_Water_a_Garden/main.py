from typing import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        t = [0] * (n + 1)
        for i, v in enumerate(ranges):
            x, y = max(i - v, 0), min(i + v, n)
            t[x] = max(t[x], y)

        res, i, j = 0, 0, 0
        while j < n:
            cur = 0
            while i <= j:
                cur = max(cur, t[i])
                i += 1

            res += 1
            if cur <= j:
                return -1

            j = cur

        return res
