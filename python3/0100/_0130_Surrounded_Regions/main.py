from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def bfs(u, v):
            q = [(u, v)]
            while q:
                u, v = q.pop(0)
                if 0 <= u < m and 0 <= v < n and board[u][v] == 'O':
                    board[u][v] = 'T'
                    q.append((u + 1, v))
                    q.append((u - 1, v))
                    q.append((u, v + 1))
                    q.append((u, v - 1))

        m, n = len(board), len(board[0])
        for i in range(m):
            if board[i][0] == 'O':
                bfs(i, 0)
            if board[i][n - 1] == 'O':
                bfs(i, n - 1)

        for j in range(n):
            if board[0][j] == 'O':
                bfs(0, j)
            if board[m - 1][j] == 'O':
                bfs(m - 1, j)

        for i in range(m):
            for j in range(n):
                board[i][j] = 'O' if board[i][j] == 'T' else 'X'
