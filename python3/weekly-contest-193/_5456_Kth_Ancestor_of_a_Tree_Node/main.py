from typing import List
import math


class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.step = int(math.log(n, 2))  # max depth is n
        self.jump = [dict(enumerate(parent))]

        for _ in range(self.step):
            cur, nxt = self.jump[-1], dict()
            for node in cur:
                if cur[node] in cur:
                    nxt[node] = cur[cur[node]]
            self.jump.append(nxt)

    def getKthAncestor(self, node: int, k: int) -> int:
        step = self.step
        while node > -1 and k > 0:
            if k >= 1 << step:
                node = self.jump[step].get(node, -1)
                k -= 1 << step
            else:
                step -= 1
        return node
