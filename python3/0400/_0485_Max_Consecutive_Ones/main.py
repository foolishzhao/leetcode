from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, i = 0, 0
        for j, v in enumerate(nums + [0]):
            if v == 0:
                res = max(res, j - i)
                i = j + 1

        return res
