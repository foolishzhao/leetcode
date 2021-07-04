import collections


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        dt = collections.defaultdict(int)
        for i in range(lowLimit, highLimit + 1):
            x = 0
            while i:
                x += i % 10
                i //= 10
            dt[x] += 1
        return max(dt.values())
