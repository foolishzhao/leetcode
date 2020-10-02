from typing import List
import collections


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0

        counter = collections.Counter(nums)
        res = 0
        for num, cnt in counter.items():
            if not k:
                res += 1 if cnt > 1 else 0
            elif num - k in counter:
                res += 1
        return res
