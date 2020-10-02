from typing import List
import functools


class Solution:
    # dp(i, j, k) represents max points can get with k boxes of same color as boxes[i] to its left
    def removeBoxes(self, boxes: List[int]) -> int:
        @functools.lru_cache(None)
        def dp(i, j, k):
            if i > j:
                return 0

            res = (k + 1) * (k + 1) + dp(i + 1, j, 0)
            for t in range(i + 1, j + 1):
                if boxes[t] == boxes[i]:
                    res = max(res, dp(i + 1, t - 1, 0) + dp(t, j, k + 1))
            return res

        return dp(0, len(boxes) - 1, 0)

    # dp(i, j, k) represents max points can get with k boxes of same color as boxes[i] to its left
    # prune the calculation
    def removeBoxes2(self, boxes: List[int]) -> int:
        @functools.lru_cache(None)
        def dp(i, j, k):
            if i > j:
                return 0

            while i + 1 <= j and boxes[i + 1] == boxes[i]:
                i += 1
                k += 1

            res = (k + 1) * (k + 1) + dp(i + 1, j, 0)
            for t in range(i + 1, j + 1):
                if boxes[t] == boxes[i] and boxes[t - 1] != boxes[i]:
                    res = max(res, dp(i + 1, t - 1, 0) + dp(t, j, k + 1))
            return res

        return dp(0, len(boxes) - 1, 0)
