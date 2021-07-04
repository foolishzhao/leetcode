from typing import List


class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[0] - x[1])
        res, cur = 0, 0
        for actual, mini in tasks:
            if cur < mini:
                res += mini - cur
                cur = mini
            cur -= actual
        return res
