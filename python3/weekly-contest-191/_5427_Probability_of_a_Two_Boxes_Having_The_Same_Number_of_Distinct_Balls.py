from typing import List
import functools


# Timeout exceed
class Solution:
    def __init__(self):
        self.eq = 0
        self.total = 0

    def getProbability(self, balls: List[int]) -> float:
        bag = list()
        for i, nb in enumerate(balls):
            for _ in range(nb):
                bag.append(1 << i)

        self.dfs(bag, 0, 0, 0, 0, 0)
        return self.eq / self.total

    def dfs(self, bag, pos, box1, n1, box2, n2):
        def nBit(box):
            res = 0
            while box > 0:
                res += 1
                box &= (box - 1)
            return res

        n = len(bag) // 2
        if n1 == n and n2 == n:
            if nBit(box1) == nBit(box2):
                self.eq += 1
            self.total += 1
            return

        if n1 < n:
            self.dfs(bag, pos + 1, box1 | bag[pos], n1 + 1, box2, n2)
        if n2 < n:
            self.dfs(bag, pos + 1, box1, n1, box2 | bag[pos], n2 + 1)


class Solution2:
    def getProbability(self, balls: List[int]) -> float:
        @functools.lru_cache(None)
        def factorial(n):
            return 1 if n == 0 else factorial(n - 1) * n

        def calcCnr(n, r):
            return factorial(n) / (factorial(r) * factorial(n - r))

        # nb1: number of balls in box1
        # nb2: number of balls in box2
        # ndb1: number of distinct balls in box1
        # ndb2: number of distinct balls in box2
        # return 1: total combination
        # return 2: valid combination
        def dfs(pos, nb1, ndb1, nb2, ndb2):
            if pos == len(balls):
                return nb1 == nb2, nb1 == nb2 and ndb1 == ndb2

            t, v, cnt = 0, 0, balls[pos]
            for i in range(cnt + 1):
                ndb1Delta, ndb2Delta = i > 0, i < cnt
                ct, cv = dfs(pos + 1, nb1 + i, ndb1 + ndb1Delta, nb2 + cnt - i, ndb2 + ndb2Delta)
                t += ct * calcCnr(cnt, i)
                v += cv * calcCnr(cnt, i)
            return t, v

        total, valid = dfs(0, 0, 0, 0, 0)
        return valid / total


if __name__ == '__main__':
    Solution2().getProbability(
        [1, 1],
    )
