from typing import List


class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        m, n = len(M), len(M[0])
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                s, c = 0, 0
                for u in [-1, 0, 1]:
                    for v in [-1, 0, 1]:
                        if 0 <= i + u < m and 0 <= j + v < n:
                            s += M[i + u][j + v]
                            c += 1
                res[i][j] = s // c
        return res

    def imageSmoother2(self, M: List[List[int]]) -> List[List[int]]:
        m, n = len(M), len(M[0])
        for i in range(m):
            for j in range(n):
                s, c = 0, 0
                for u in [-1, 0, 1]:
                    for v in [-1, 0, 1]:
                        if 0 <= i + u < m and 0 <= j + v < n:
                            s += M[i + u][j + v] & 0xff
                            c += 1
                M[i][j] |= (s // c) << 0xff

        for i in range(m):
            for j in range(n):
                M[i][j] >>= 0xff
        return M
