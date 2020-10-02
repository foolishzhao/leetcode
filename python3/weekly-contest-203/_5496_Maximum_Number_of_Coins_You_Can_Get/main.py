from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        return sum(sorted(piles)[n // 3:][::2])
