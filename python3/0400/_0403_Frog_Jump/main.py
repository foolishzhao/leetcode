from typing import List
import collections


class Solution:
    def __init__(self):
        self.memo = dict()

    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False

        n = len(stones)
        return self.dfs(set(stones), 1, stones[-1], 1)

    def dfs(self, stones, lastStone, target, lastJump):
        if lastStone == target:
            return True

        if (lastStone, lastJump) in self.memo:
            return self.memo[(lastStone, lastJump)]

        for i in [-1, 0, 1]:
            nextStone = lastStone + lastJump + i
            if nextStone > lastStone and nextStone in stones:
                if self.dfs(stones, nextStone, target, lastJump + i):
                    self.memo[(lastStone, lastJump)] = True
                    return True

        self.memo[(lastStone, lastJump)] = False
        return False

    def canCross2(self, stones: List[int]) -> bool:
        steps = collections.defaultdict(set)
        steps[0].add(1)

        st = set(stones)
        for stone in stones:
            for step in steps[stone]:
                nxt = stone + step
                if nxt == stones[-1]:
                    return True

                if nxt in st:
                    steps[nxt].add(step)
                    if step > 1:
                        steps[nxt].add(step - 1)
                    steps[nxt].add(step + 1)

        return False
