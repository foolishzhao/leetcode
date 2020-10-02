from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        self.parent[ry] = rx
        return True


class Solution:
    # two cases
    # case 1: no node has two parents, must form a circle
    # case 2: one node has two parents, must remove one of two parents
    #
    # for case 1: use union find to detect the circle
    # for case 2: skip secE, use union find to detect circle, return firE if detected else secE
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [0] * (n + 1)
        firE, secE = None, None
        for u, v in edges:
            if parent[v]:
                firE = [parent[v], v]
                secE = [u, v]
                break
            parent[v] = u

        uf = UnionFind(n + 1)
        for u, v in edges:
            if [u, v] == secE:
                continue

            if not uf.union(u, v):
                return firE if firE else [u, v]

        return secE

    # make code logic more clear
    def findRedundantDirectedConnection2(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [0] * (n + 1)
        firE, secE = None, None
        for u, v in edges:
            if parent[v]:
                firE = [parent[v], v]
                secE = [u, v]
                break
            parent[v] = u

        uf = UnionFind(n + 1)
        if not firE:
            for u, v in edges:
                if not uf.union(u, v):
                    return [u, v]
        else:
            for u, v in edges:
                if [u, v] == secE:
                    continue
                if not uf.union(u, v):
                    return firE
            return secE
