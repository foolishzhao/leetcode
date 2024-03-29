from typing import List
import bisect


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        res, li = list(), list()
        for x in obstacles:
            if not li or x >= li[-1]:
                li.append(x)
                res.append(len(li))
            else:
                idx = bisect.bisect_right(li, x)
                res.append(idx + 1)
                li[idx] = x

        return res
