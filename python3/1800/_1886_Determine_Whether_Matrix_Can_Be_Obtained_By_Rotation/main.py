from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(m):
            res = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    res[i][j] = m[n - j - 1][i]
            return res

        n = len(mat)
        return target in (mat, rotate(mat), rotate(rotate(mat)), rotate(rotate(rotate(mat))))
