from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parent[px] = py


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def similar(s1, s2):
            diff = sum([x != y for x, y in zip(s1, s2)])
            return diff == 0 or diff == 2

        n = len(strs)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(i + 1, n):
                if similar(strs[i], strs[j]):
                    uf.union(i, j)

        return len({uf.find(i) for i in range(n)})
