from typing import List
import collections


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        def dfs1(x, prev):
            for y in graph[x]:
                if y != prev:
                    dfs1(y, x)
                    res[x] += res[y] + count[y]
                    count[x] += count[y]

        def dfs2(x, prev):
            for y in graph[x]:
                if y != prev:
                    res[y] = res[x] - count[y] + n - count[y]
                    dfs2(y, x)

        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        res, count = [0] * n, [1] * n
        dfs1(0, -1)
        dfs2(0, -1)

        return res
