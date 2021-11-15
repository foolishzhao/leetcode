from typing import List


class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        res, i, n, cur = 0, 0, len(rungs), 0
        while i < n:
            if rungs[i] - cur <= dist:
                cur = rungs[i]
                i += 1
            else:
                step = (rungs[i] - cur - 1) // dist
                cur += step * dist
                res += step

        return res
