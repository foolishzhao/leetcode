from typing import List
import heapq


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pq, curMax = list(), float('-inf')
        for i, li in enumerate(nums):
            heapq.heappush(pq, (li[0], i, 0))
            curMax = max(curMax, li[0])

        l, s = float('inf'), 0
        while True:
            curMin, i, j = heapq.heappop(pq)
            if curMax - curMin < l:
                l = curMax - curMin
                s = curMin

            if j < len(nums[i]) - 1:
                heapq.heappush(pq, (nums[i][j + 1], i, j + 1))
                curMax = max(curMax, nums[i][j + 1])
            else:
                break

        return [s, s + l]
