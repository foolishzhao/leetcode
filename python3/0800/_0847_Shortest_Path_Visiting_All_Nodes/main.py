from typing import List


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n, q = len(graph), list()

        seen = set()
        for i in range(n):
            mask = 1 << i
            q.append((mask, i, 0))
            seen.add((mask, i))

        while q:
            mask, i, p = q.pop(0)
            if mask == (1 << n) - 1:
                return p

            for j in graph[i]:
                nxtMask = mask | (1 << j)
                if (nxtMask, j) not in seen:
                    seen.add((nxtMask, j))
                    q.append((nxtMask, j, p + 1))
