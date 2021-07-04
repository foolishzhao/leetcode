from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n, res = len(matrix), len(matrix[0]), 0

        accum = [[0] * n for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                accum[i + 1][j] = accum[i][j] + 1 if matrix[i][j] else 0

        for row in accum:
            row.sort(reverse=True)
            for i in range(n):
                res = max(res, row[i] * (i + 1))
                if not row[i]:
                    break

        return res
