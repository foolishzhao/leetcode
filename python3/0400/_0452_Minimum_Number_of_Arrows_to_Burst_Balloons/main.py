from typing import List


class Solution:
    # The problem is the same as "Given a collection of intervals,
    # find the maximum number of intervals that are non-overlapping."
    # [[2,4], [1,4], [1,5], [3,6], [7,10]]
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[1])

        res, curEnd = 0, float('-inf')
        for start, end in points:
            if start > curEnd:
                res += 1
                curEnd = end

        return res
