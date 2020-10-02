from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        a, b = m, n
        for x, y in ops:
            a = min(a, x)
            b = min(b, y)
        return a * b
