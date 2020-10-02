from typing import List


class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        n = len(candies)
        unique = len(set(candies))
        return min(unique, n // 2)
