from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0

        res = duration
        for t1, t2 in zip(timeSeries[:-1], timeSeries[1:]):
            res += min(t2 - t1, duration)
        return res
