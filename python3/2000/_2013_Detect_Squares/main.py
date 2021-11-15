from typing import List
import collections


class DetectSquares:

    def __init__(self):
        self.xs = collections.defaultdict(list)
        self.ps = collections.defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.ps[tuple(point)] += 1
        self.xs[point[0]].append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        for xp in self.xs[point[0]]:
            if xp[1] == point[1]:
                continue

            dist = abs(point[1] - xp[1])

            res += self.ps[(point[0] + dist, xp[1])] * self.ps[(point[0] + dist, point[1])]
            res += self.ps[(point[0] - dist, xp[1])] * self.ps[(point[0] - dist, point[1])]
        return res
