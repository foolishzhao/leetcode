from typing import List


class UnionFind:
    def __init__(self, n):
        self.n = n
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
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        mat = [[0] * col for _ in range(row)]
        for x, y in cells:
            mat[x - 1][y - 1] = 1

        uf = UnionFind(row * col + 2)
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    for movI, movJ in [[0, 1], [1, 0]]:
                        ni, nj = i + movI, j + movJ
                        if 0 <= ni < row and 0 <= nj < col and mat[ni][nj] == 0:
                            uf.union(i * col + j + 1, ni * col + nj + 1)

        d = len(cells)
        while d:
            if uf.find(0) == uf.find(row * col + 1):
                break

            i, j = cells[d - 1][0] - 1, cells[d - 1][1] - 1
            mat[i][j] = 0

            if i == 0:
                uf.union(0, j + 1)
            if i == row - 1:
                uf.union((row - 1) * col + j + 1, row * col + 1)

            for movI, movJ in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                ni, nj = i + movI, j + movJ
                if 0 <= ni < row and 0 <= nj < col and mat[ni][nj] == 0:
                    uf.union(i * col + j + 1, ni * col + nj + 1)

            d -= 1
        return d
