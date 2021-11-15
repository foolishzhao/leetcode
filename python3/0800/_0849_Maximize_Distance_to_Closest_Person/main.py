from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        prev, n, res = -1, len(seats), 1

        for i, seat in enumerate(seats):
            if seat:
                if prev == -1:
                    res = max(res, i)
                else:
                    res = max(res, (i - prev) // 2)
                prev = i
        return max(res, n - 1 - prev)
