from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n, res = len(mat), len(mat[0]), 0
        for j in range(n):
            for i in range(m):
                if mat[i][j] == 1:
                    s = sum([mat[i][k] for k in range(n)])
                    s += sum([mat[k][j] for k in range(m)])
                    res += s == 2
                    break
        return res
