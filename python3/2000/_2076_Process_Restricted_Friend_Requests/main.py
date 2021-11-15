from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

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
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        uf, res = UnionFind(n), list()
        for u, v in requests:
            pu, pv = uf.find(u), uf.find(v)
            if pu == pv:
                res.append(True)
                continue

            check = True
            for x, y in restrictions:
                px, py = uf.find(x), uf.find(y)
                if (px == pu and py == pv) or (px == pv and py == pu):
                    check = False
                    break
            if check:
                uf.union(pu, pv)
                res.append(True)
            else:
                res.append(False)
        return res
