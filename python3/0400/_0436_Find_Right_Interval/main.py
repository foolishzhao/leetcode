from typing import List
import bisect


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        res = list()
        if not intervals:
            return res

        startsAndIndex = sorted((p[0], i) for i, p in enumerate(intervals))
        starts = [x[0] for x in startsAndIndex]
        for _, end in intervals:
            i = bisect.bisect_left(starts, end)
            res.append(-1 if i == len(starts) else startsAndIndex[i][1])

        return res


if __name__ == '__main__':
    Solution().findRightInterval([[1, 2]])
