from typing import List


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            rx, ry = self.rank[px], self.rank[py]
            if rx <= ry:
                self.parent[px] = py
                if rx == ry:
                    self.rank[py] += 1
            else:
                self.parent[py] = px


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edges = sorted([(w, u, v) for (u, v, w) in edgeList])
        queries = sorted([(l, p, q, i) for i, (p, q, l) in enumerate(queries)])
        uf, ii = UnionFind(n), 0
        res = [None] * len(queries)
        for l, p, q, i in queries:
            while ii < len(edges) and edges[ii][0] < l:
                _, u, v = edges[ii]
                uf.union(u, v)
                ii += 1
            res[i] = uf.find(p) == uf.find(q)
        return res
