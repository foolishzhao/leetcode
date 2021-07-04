from typing import List
import bisect


class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(candiesCount)

        candies = [0] * n
        candies[0] = candiesCount[0]
        for i in range(1, n):
            candies[i] = candies[i - 1] + candiesCount[i]

        res = list()
        for t, d, c in queries:
            mn, mx = d + 1, (d + 1) * c
            leftIdx = bisect.bisect_left(candies, mn)
            rightIdx = bisect.bisect_left(candies, mx)
            res.append(leftIdx <= t <= rightIdx)
        return res

    def canEat2(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(candiesCount)

        candies = [0] * (n + 1)
        for i in range(n):
            candies[i + 1] = candies[i] + candiesCount[i]

        # min day: (candies[t] // c + 1) - 1
        # max day: candies[t + 1] - 1 (take note it's zero indexed)
        return [candies[t] // c <= d < candies[t + 1] for t, d, c in queries]
