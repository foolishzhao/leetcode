from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n, res = len(matrix), len(matrix[0]), 0
        dt = dict()
        for i in range(m):
            for j in range(n):
                res = max(res, self.dfs(matrix, dt, i, j))

        return res

    def dfs(self, matrix, dt, i, j):
        m, n = len(matrix), len(matrix[0])

        if (i, j) not in dt:
            res = 1
            for u, v in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                ni, nj = i + u, j + v
                if ni < 0 or ni >= m or nj < 0 or nj >= n:
                    continue

                # must check if condition to avoid recursive call
                if matrix[ni][nj] > matrix[i][j]:
                    res = max(res, 1 + self.dfs(matrix, dt, ni, nj))

            dt[(i, j)] = res

        return dt[(i, j)]


if __name__ == '__main__':
    Solution().longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]])
