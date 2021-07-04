from typing import List
import heapq


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        pq = list()
        for num in nums:
            if num % 2 == 1:
                heapq.heappush(pq, (num, num * 2))
            else:
                upper = num
                while num % 2 == 0:
                    num >>= 1
                heapq.heappush(pq, (num, upper))

        maxLower = max([x[0] for x in pq])
        res = maxLower - pq[0][0]
        while True:
            cur, upper = heapq.heappop(pq)
            if cur >= upper:
                break

            cur <<= 1
            maxLower = max(maxLower, cur)
            heapq.heappush(pq, (cur, upper))
            res = min(res, maxLower - pq[0][0])

        return res
