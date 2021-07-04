from typing import List
import collections


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        outD, inNode = [0] * n, collections.defaultdict(list)
        res, q = list(), list()

        for u, vs in enumerate(graph):
            outD[u] = len(vs)
            if outD[u] == 0:
                q.append(u)
            for v in vs:
                inNode[v].append(u)

        while q:
            u = q.pop(0)
            res.append(u)

            for v in inNode[u]:
                outD[v] -= 1
                if outD[v] == 0:
                    q.append(v)

        return sorted(res)
