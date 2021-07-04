from typing import List
import collections


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dt, res = collections.defaultdict(int), 0
        for num in nums:
            if dt[k - num] > 0:
                res += 1
                dt[k - num] -= 1
            else:
                dt[num] += 1
        return res
