from typing import List


class Solution:
    # The problem is the same as "Given a collection of intervals,
    # find the maximum number of intervals that are non-overlapping."
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])

        count, curEnd = 0, float('-inf')
        for start, end in intervals:
            if start >= curEnd:
                count += 1
                curEnd = end

        return len(intervals) - count
