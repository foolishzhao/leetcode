from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.size[py] += self.size[px]
            self.parent[px] = py

    def count(self, x):
        return self.size[self.find(x)]


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        uf = UnionFind(n * n)

        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    uf.size[i * n + j] = 1
                    for di, dj in [[-1, 0], [0, -1]]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj]:
                            uf.union(i * n + j, ni * n + nj)

        res = max([uf.count(x) for x in range(n * n)])
        for i in range(n):
            for j in range(n):
                if not grid[i][j]:
                    ps = set()
                    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj]:
                            ps.add(uf.find(ni * n + nj))
                    res = max(res, sum([uf.count(p) for p in ps]) + 1)
        return res
