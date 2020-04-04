from typing import List
import collections


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()

        m, n = len(matrix), len(matrix[0])
        dt = collections.defaultdict(list)
        for i in range(m):
            for j in range(n):
                dt[i + j].append(matrix[i][j])

        res = list()
        for i in range(m + n - 1):
            res.extend(dt[i] if i % 2 == 1 else dt[i][::-1])
        return res

    def findDiagonalOrder2(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()

        m, n, i, j, d = len(matrix), len(matrix[0]), 0, 0, 1
        res = list()
        for _ in range(m * n):
            res.append(matrix[i][j])
            i -= d
            j += d
            # if i >= m and j < 0 both satisfies, handle i >= m case
            if i >= m:
                i, d = m - 1, -d
                j += 2
            # if j >= n and i < 0 both satisfies, handle j >= n case
            if j >= n:
                j, d = n - 1, -d
                i += 2
            if i < 0:
                i, d = 0, -d
            if j < 0:
                j, d = 0, -d

        return res
