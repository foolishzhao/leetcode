from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n, res = len(mat), len(mat[0]), 0
        h = [0] * n
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    h[j] += 1
                    res += h[j]

                    k, mh = j - 1, h[j]
                    while k >= 0 and h[k]:
                        mh = min(mh, h[k])
                        res += mh
                        k -= 1
                else:
                    h[j] = 0
        return res
