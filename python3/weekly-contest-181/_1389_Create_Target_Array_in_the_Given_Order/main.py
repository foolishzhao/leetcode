from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = list()
        for x, i in zip(nums, index):
            res.insert(i, x)

        return res
