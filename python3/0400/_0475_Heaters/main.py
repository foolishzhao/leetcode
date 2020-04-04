from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters = [float('-inf')] + sorted(heaters) + [float('inf')]

        res, j = 0, 1
        for h in sorted(houses):
            while h >= heaters[j]:
                j += 1
            res = max(res, min(h - heaters[j - 1], heaters[j] - h))

        return res
