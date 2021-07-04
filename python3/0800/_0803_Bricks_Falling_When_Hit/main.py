from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parent[px] = py
            self.size[py] += self.size[px]

    def count(self, x):
        px = self.find(x)
        return self.size[px]


class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        for x, y in hits:
            if grid[x][y] == 1:
                grid[x][y] = 2

        def connect(u, v):
            pos = u * n + v + 1
            for du, dv in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nu, nv = u + du, v + dv
                if 0 <= nu < m and 0 <= nv < n and grid[nu][nv] == 1:
                    uf.union(pos, nu * n + nv + 1)

            if u == 0:
                uf.union(pos, 0)

        uf = UnionFind(m * n + 1)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    connect(i, j)

        left = uf.count(0)
        res = list()
        for x, y in reversed(hits):
            if grid[x][y] == 2:
                grid[x][y] = 1
                connect(x, y)
                newLeft = uf.count(0)
                res.append(max(newLeft - left - 1, 0))
                left = newLeft
            else:
                res.append(0)

        return res[::-1]
