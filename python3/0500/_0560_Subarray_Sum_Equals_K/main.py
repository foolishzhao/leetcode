from typing import List
import collections


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = collections.defaultdict(int)
        prefix[0] = 1

        res, cur = 0, 0
        for num in nums:
            cur += num
            res += prefix[cur - k]
            prefix[cur] += 1

        return res
