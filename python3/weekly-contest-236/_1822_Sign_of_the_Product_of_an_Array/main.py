from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res = 1
        for num in nums:
            if num < 0:
                res *= -1
            elif num == 0:
                return 0
        return res
