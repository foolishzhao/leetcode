from typing import List
from queue import Queue


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])
        q = Queue()

        for i in range(m):
            if board[i][0] == 'O':
                q.put((i, 0))
            if board[i][n - 1] == 'O':
                q.put((i, n - 1))

        for i in range(1, n - 1):
            if board[0][i] == 'O':
                q.put((0, i))
            if board[m - 1][i] == 'O':
                q.put((m - 1, i))

        while not q.empty():
            i, j = q.get()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'T'
                q.put((i - 1, j))
                q.put((i + 1, j))
                q.put((i, j - 1))
                q.put((i, j + 1))

        for i in range(m):
            for j in range(n):
                board[i][j] = 'O' if board[i][j] == 'T' else 'X'
