from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        curMin, res = float('inf'), 0
        for num in nums:
            curMin = min(curMin, num)
            res = max(res, num - curMin)
        return res if res else -1
