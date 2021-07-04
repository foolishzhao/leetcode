from typing import List
import collections


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.rank[px] > self.rank[py]:
                self.parent[py] = px
            else:
                self.parent[px] = py
                self.rank[py] += self.rank[px] == self.rank[py]


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        uf = UnionFind(n)
        for u, v in allowedSwaps:
            uf.union(u, v)

        group = collections.defaultdict(list)
        for i, g in enumerate(uf.parent):
            group[uf.find(g)].append(i)

        res = 0
        for grp in group.values():
            dt = collections.defaultdict(int)
            for i in grp:
                dt[source[i]] += 1
            for i in grp:
                if dt[target[i]] > 0:
                    dt[target[i]] -= 1
            res += sum(dt.values())
        return res
