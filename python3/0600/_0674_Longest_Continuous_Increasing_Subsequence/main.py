from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res, prev, curLen = 0, float('-inf'), 0
        for num in nums:
            if num > prev:
                curLen += 1
                res = max(res, curLen)
            else:
                curLen = 1
            prev = num
        return res
