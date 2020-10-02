import collections
from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        def dfs(u):
            res = 0
            for v in e[u]:
                res += dfs(v)
            return res + 2 if hasApple[u] or res else res

        e = collections.defaultdict(list)
        for x, y in edges:
            e[x].append(y)
        res = dfs(0)
        return res - 2 if res else 0
