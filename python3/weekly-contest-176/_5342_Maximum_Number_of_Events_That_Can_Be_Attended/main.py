from typing import List
import heapq


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()

        res, i, n = 0, 0, len(events)
        pq = list()
        for d in range(1, 100001):
            while i < n and events[i][0] == d:
                heapq.heappush(pq, events[i][1])
                i += 1

            while pq and pq[0] < d:
                heapq.heappop(pq)

            if pq:
                res += 1
                heapq.heappop(pq)

        return res


if __name__ == '__main__':
    print(Solution().maxEvents([[1, 3], [1, 3], [1, 3], [3, 4]]))
