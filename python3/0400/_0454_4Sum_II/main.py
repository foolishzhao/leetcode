from typing import List
import collections


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        dt = collections.defaultdict(int)
        for a in A:
            for b in B:
                dt[a + b] += 1

        res = 0
        for c in C:
            for d in D:
                res += dt[-c - d]

        return res
