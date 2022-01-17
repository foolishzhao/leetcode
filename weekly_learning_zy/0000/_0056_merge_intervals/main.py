from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]
        for i in intervals:
            if i[0] > ans[-1][1]:
                ans.append(i)
            else:
                ans[-1][1] = max(ans[-1][1], i[1])
        return ans