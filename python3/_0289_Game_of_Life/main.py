from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                cnt = 0
                for u in [-1, 0, 1]:
                    for v in [-1, 0, 1]:
                        if u == 0 and v == 0:
                            continue

                        if i + u < 0 or i + u >= m or j + v < 0 or j + v >= n:
                            continue

                        if board[i + u][j + v] & 1:
                            cnt += 1

                if board[i][j] and (cnt == 2 or cnt == 3):
                    board[i][j] |= 2
                elif not board[i][j] and cnt == 3:
                    board[i][j] |= 2

        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1
