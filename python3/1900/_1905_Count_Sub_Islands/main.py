from typing import List
import collections


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.child = collections.defaultdict(list)
        for i in range(n):
            self.child[i].append(i)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.rank[px] <= self.rank[py]:
                self.parent[px] = py
                for c in self.child[px]:
                    self.child[py].append(c)
                del self.child[px]

                if self.rank[px] == self.rank[py]:
                    self.rank[py] += 1
            else:
                self.parent[py] = px
                for c in self.child[py]:
                    self.child[px].append(c)
                del self.child[py]


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])
        uf1, uf2 = UnionFind(m * n), UnionFind(m * n)
        for i in range(m):
            for j in range(n):
                if grid1[i][j] == 1:
                    for di, dj in [[-1, 0], [0, -1]]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n and grid1[ni][nj] == 1:
                            uf1.union(i * n + j, ni * n + nj)

                if grid2[i][j] == 1:
                    for di, dj in [[-1, 0], [0, -1]]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n and grid2[ni][nj] == 1:
                            uf2.union(i * n + j, ni * n + nj)

        res = 0
        for child in uf2.child.values():
            ps, valid = set(), True
            for x in child:
                rx, cx = x // n, x % n
                if grid2[rx][cx] == 0 or grid1[rx][cx] == 0:
                    valid = False
                    break

                ps.add(uf1.find(x))

            res += valid and len(ps) == 1
        return res

    def countSubIslands2(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(u, v):
            if not (0 <= u < m and 0 <= v < n and grid2[u][v] == 1):
                return 1

            grid2[u][v] = 0
            res = grid1[u][v]
            for du, dv in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                res &= dfs(u + du, v + dv)
            return res

        m, n = len(grid1), len(grid1[0])
        return sum([dfs(i, j) for i in range(m) for j in range(n) if grid2[i][j] == 1])
