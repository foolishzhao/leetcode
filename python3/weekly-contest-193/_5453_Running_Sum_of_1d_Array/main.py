from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        cur, res = 0, list()
        for num in nums:
            cur += num
            res.append(cur)
        return res
