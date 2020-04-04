from typing import List
import collections


class Solution:
    def __init__(self):
        self.memo = dict()

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        edges = collections.defaultdict(list)
        for p, v in zip(equations, values):
            a, b = p[0], p[1]
            edges[a].append((b, v))
            edges[b].append((a, 1 / v))
            self.memo[(a, b)] = v
            self.memo[(b, a)] = 1 / v

        res = list()
        for a, b in queries:
            if a not in edges or b not in edges:
                res.append(-1.0)
            elif a == b:
                res.append(1.0)
            else:
                res.append(self.dfs(edges, a, b, set()))

        return res

    def dfs(self, edges, a, b, visited):
        if a == b:
            return v

        if (a, b) in self.memo:
            return self.memo[(a, b)]

        visited.add(a)
        res = -1.0
        for nxt, cost in edges[a]:
            if nxt not in visited:
                curRes = self.dfs(edges, nxt, b, visited)
                if curRes != -1:
                    res = curRes * cost
                    break

        self.memo[(a, b)] = res
        return res
