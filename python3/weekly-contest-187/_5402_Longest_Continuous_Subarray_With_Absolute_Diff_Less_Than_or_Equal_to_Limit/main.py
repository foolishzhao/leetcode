from typing import List
import bisect
import collections


class Solution:
    # time complexity O(n^2), space complexity O(n)
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res, i = 0, 0
        cur = list()
        for j, num in enumerate(nums):
            bisect.insort(cur, num)
            while cur and cur[-1] - cur[0] > limit:
                idx = bisect.bisect_left(cur, nums[i])
                cur.pop(idx)
                i += 1
            res = max(res, len(cur))
        return res

    # time complexity O(n), space complexity O(n)
    def longestSubarray2(self, nums: List[int], limit: int) -> int:
        res, i = 0, 0
        maxD, minD = collections.deque(), collections.deque()
        for j, num in enumerate(nums):
            while maxD and num > maxD[-1]:
                maxD.pop()
            while minD and num < minD[-1]:
                minD.pop()
            maxD.append(num)
            minD.append(num)

            while maxD[0] - minD[0] > limit:
                if nums[i] == maxD[0]:
                    maxD.popleft()
                if nums[i] == minD[0]:
                    minD.popleft()
                i += 1

            res = max(res, j - i + 1)
        return res
