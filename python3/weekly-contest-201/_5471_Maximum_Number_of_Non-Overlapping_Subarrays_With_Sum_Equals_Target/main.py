from typing import List


class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        n = len(nums)

        res, cur, preSet = 0, 0, {0}
        for i in range(n):
            cur += nums[i]
            if cur - target in preSet:
                res += 1
                cur = 0
                preSet = {0}
            else:
                preSet.add(cur)
        return res
