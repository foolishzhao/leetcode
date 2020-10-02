from typing import List
import random


class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        self.M = N - len(blacklist)
        self.dt = dict()

        blacklist.sort()
        bset = set(blacklist)

        i = 0
        for j in range(self.M, N):
            if j not in bset:
                self.dt[blacklist[i]] = j
                i += 1

    def pick(self) -> int:
        r = random.randint(0, self.M - 1)
        return self.dt[r] if r in self.dt else r
