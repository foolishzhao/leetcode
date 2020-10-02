from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m = len(flowerbed)
        for i, v in enumerate(flowerbed):
            if v == 0:
                if (i == 0 or flowerbed[i - 1] == 0) and (i == m - 1 or flowerbed[i + 1] == 0):
                    flowerbed[i] = 1
                    n -= 1
        return n <= 0
