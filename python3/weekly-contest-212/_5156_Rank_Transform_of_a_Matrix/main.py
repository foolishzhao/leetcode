from typing import List
import collections


class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        dt = collections.defaultdict(list)
        for i in range(m):
            for j in range(n):
                dt[matrix[i][j]].append((i, j))

        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        rank = [0] * (m + n)
        for val in sorted(dt):
            p = list(range(m + n))
            rank2 = rank[:]
            for i, j in dt[val]:
                i, j = find(i), find(j + m)
                p[i] = j
                rank2[j] = max(rank2[i], rank2[j])

            for i, j in dt[val]:
                rank[i] = rank[j + m] = matrix[i][j] = rank2[find(i)] + 1

        return matrix
