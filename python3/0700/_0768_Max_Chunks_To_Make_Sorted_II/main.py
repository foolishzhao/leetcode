from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        res, s1, s2 = 0, 0, 0
        for a1, a2 in zip(arr, sorted(arr)):
            s1 += a1
            s2 += a2
            res += s1 == s2
        return res
