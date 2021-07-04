from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.rank[px] < self.rank[py]:
                self.parent[px] = py
            else:
                self.parent[py] = px
                if self.rank[px] == self.rank[py]:
                    self.rank[px] += 1


class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        if not threshold:
            return [True] * len(queries)

        uf = UnionFind(n)
        for x in range(threshold + 1, n // 2 + 1):
            i = 2
            while i * x <= n:
                uf.union(x, i * x)
                i += 1

        return [uf.find(x) == uf.find(y) for x, y in queries]
