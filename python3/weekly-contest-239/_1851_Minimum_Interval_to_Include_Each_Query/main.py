from typing import List
import heapq


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        queries = sorted(enumerate(queries), key=lambda x: x[1])
        intervals.sort()
        pq, i, res = list(), 0, [-1] * len(queries)
        for index, query in queries:
            while i < len(intervals) and intervals[i][0] <= query:
                heapq.heappush(pq, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1

            while pq and pq[0][1] < query:
                heapq.heappop(pq)

            if pq:
                res[index] = pq[0][0]
        return res
