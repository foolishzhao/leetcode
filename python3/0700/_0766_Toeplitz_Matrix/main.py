from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        def helper(u, v):
            while u + 1 < m and v + 1 < n:
                if matrix[u + 1][v + 1] != matrix[u][v]:
                    return False
                u += 1
                v += 1
            return True

        m, n = len(matrix), len(matrix[0])
        for i in range(1, n):
            if not helper(0, i):
                return False

        for i in range(0, m):
            if not helper(i, 0):
                return False

        return True

    def isToeplitzMatrix2(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        for i in range(m - 1):
            for j in range(n - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True
