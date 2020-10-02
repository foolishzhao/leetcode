from typing import List
import heapq


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        minPq, maxPq = list(), list()
        zero = False
        for num in nums:
            if num > 0:
                heapq.heappush(minPq, num)
                if len(minPq) > 3:
                    heapq.heappop(minPq)
            elif num < 0:
                heapq.heappush(maxPq, -num)
                if len(maxPq) > 3:
                    heapq.heappop(maxPq)
            else:
                zero = True

        nums = minPq + [-x for x in maxPq]
        if zero:
            nums.append(0)
        while len(nums) < 3:
            nums.append(0)

        res, n = float('-inf'), len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    res = max(res, nums[i] * nums[j] * nums[k])
        return res

    def maximumProduct2(self, nums: List[int]) -> int:
        minPq, maxPq = list(), list()
        for num in nums:
            heapq.heappush(minPq, num)
            if len(minPq) > 3:
                heapq.heappop(minPq)

            heapq.heappush(maxPq, -num)
            if len(maxPq) > 2:
                heapq.heappop(maxPq)

        return max(minPq[0] * minPq[1] * minPq[2], max(minPq) * maxPq[0] * maxPq[1])
