from typing import List


class Solution:
    def setZeroes(self, m: List[List[int]]) -> None:
        h = len(m)
        w = len(m[0])
        for r in range(h):
            for c in range(w):
                if m[r][c] == 0:
                    for i in range(h):
                        if m[i][c] != 0:
                            m[i][c] = "k"
                    for j in range(w):
                        if m[r][j] != 0:
                            m[r][j] = "k"
        for r in range(h):
            for c in range(w):
                if m[r][c] == "k":
                    m[r][c] = 0

if __name__ ==  '__main__':
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    Solution().setZeroes(matrix)
    print(matrix)
