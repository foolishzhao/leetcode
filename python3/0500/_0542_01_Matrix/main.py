from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        res = [[float('inf')] * n for _ in range(m)]
        q = list()
        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    q.append((i, j, 0))

        while q:
            i, j, d = q.pop(0)
            if 0 <= i < m and 0 <= j < n and d < res[i][j]:
                res[i][j] = d
                for mi, mj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    q.append((i + mi, j + mj, d + 1))
        return res
