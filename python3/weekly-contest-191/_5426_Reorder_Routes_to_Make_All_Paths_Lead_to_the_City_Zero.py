from typing import List
import collections


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edge = collections.defaultdict(list)
        for u, v in connections:
            edge[v].append((u, 1))
            edge[u].append((v, -1))

        res, q, visited = 0, [0], {0}
        while q:
            x = q.pop(0)
            for y, d in edge[x]:
                if y not in visited:
                    visited.add(y)
                    q.append(y)
                    res += d < 0
        return res
