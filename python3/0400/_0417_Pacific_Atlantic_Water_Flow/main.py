from typing import List


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        res = list()
        if not matrix or not matrix[0]:
            return res

        m, n = len(matrix), len(matrix[0])
        pacific = [[0] * n for _ in range(m)]
        atlantic = [[0] * n for _ in range(m)]

        for i in range(m):
            pacific[i][0] = 1
            atlantic[i][n - 1] = 1

        for i in range(n):
            pacific[0][i] = 1
            atlantic[m - 1][i] = 1

        for i in range(m):
            for j in range(n):
                if pacific[i][j] == 0:
                    if not self.dfs(matrix, pacific, i, j, set()):
                        pacific[i][j] = -1
                if atlantic[i][j] == 0:
                    if not self.dfs(matrix, atlantic, i, j, set()):
                        atlantic[i][j] = -1

        for i in range(m):
            for j in range(n):
                if pacific[i][j] == 1 and atlantic[i][j] == 1:
                    res.append([i, j])

        return res

    def dfs(self, matrix, ocean, i, j, visited):
        if ocean[i][j] != 0:
            return ocean[i][j]

        visited.add((i, j))
        m, n = len(matrix), len(matrix[0])
        for mi, mj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            ni, nj = i + mi, j + mj
            if 0 <= ni < m and 0 <= nj < n and matrix[i][j] >= matrix[ni][nj] and (ni, nj) not in visited:
                curRes = self.dfs(matrix, ocean, ni, nj, visited)
                if curRes == 1:
                    ocean[i][j] = 1
                    return 1

        # why not set ocean[i][j] to -1 and return -1?
        # consider the case where last row is [7, 8, 9, 10]
        # when process 8, it dfs to 9, coz 8 is visited, so 9 can't dfs to it to avoid circle.
        # but 9 can succeed through 8, so only can set to 0 here.
        return 0


class Solution2:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        res = list()
        if not matrix or not matrix[0]:
            return res

        m, n = len(matrix), len(matrix[0])
        pf = [[0] * n for _ in range(m)]
        af = [[0] * n for _ in range(m)]

        pq, aq = list(), list()
        for i in range(m):
            pq.append((i, 0))
            aq.append((i, n - 1))

        for i in range(n):
            pq.append((0, i))
            aq.append((m - 1, i))

        self.bfs(matrix, m, n, pq, pf)
        self.bfs(matrix, m, n, aq, af)

        for i in range(m):
            for j in range(n):
                if pf[i][j] == 1 and af[i][j] == 1:
                    res.append([i, j])

        return res

    def bfs(self, matrix, m, n, q, f):
        while q:
            i, j = q.pop()
            f[i][j] = 1
            for mi, mj in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                ni, nj = i + mi, j + mj
                if 0 <= ni < m and 0 <= nj < n and f[ni][nj] == 0 and matrix[ni][nj] >= matrix[i][j]:
                    q.append((ni, nj))
