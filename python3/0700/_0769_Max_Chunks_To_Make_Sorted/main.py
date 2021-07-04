from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        res, i, cur, n = 0, 0, 0, len(arr)
        while i < n:
            cur = max(cur, arr[i])
            i += 1
            if i > cur:
                res += 1
        return res

    def maxChunksToSorted2(self, arr: List[int]) -> int:
        res, cur = 0, 0
        for i, a in enumerate(arr):
            cur = max(cur, a)
            res += cur == i
        return res
