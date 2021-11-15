from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pt = [(p, (target - p) / s) for p, s in zip(position, speed)]
        pt.sort()

        res, curT = 0, 0
        for _, t in pt[::-1]:
            if t > curT:
                res += 1
                curT = t
        return res
