from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        tx, ty, tz = target
        mx, my, mz = 0, 0, 0

        for x, y, z in triplets:
            if x <= tx and y <= ty and z <= tz:
                mx = max(mx, x)
                my = max(my, y)
                mz = max(mz, z)

        return mx == tx and my == ty and mz == tz
