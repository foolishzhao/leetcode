from typing import List
import heapq


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        curSum = sum(target)

        pq = list()
        for x in target:
            heapq.heappush(pq, -x)

        while pq:
            curMax = -heapq.heappop(pq)
            if curMax == 1:
                return True

            otherSum = curSum - curMax
            if curMax <= otherSum:
                return False

            nxt = curMax % otherSum
            curSum = otherSum + nxt

            heapq.heappush(pq, -nxt)
