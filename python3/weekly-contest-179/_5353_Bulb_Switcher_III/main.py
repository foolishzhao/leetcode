from typing import List


class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        res, curMax = 0, 0
        for i, v in enumerate(light):
            curMax = max(curMax, v)
            if i == curMax - 1:
                res += 1

        return res
