from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        x, y = click[0], click[1]
        if board[x][y] == 'M':
            board[x][y] = 'X'
        elif board[x][y] == 'E':
            m, n, mine = len(board), len(board[0]), 0
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    nx, ny = x + i, y + j
                    if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'M':
                        mine += 1

            if not mine:
                board[x][y] = 'B'
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        nx, ny = x + i, y + j
                        if 0 <= nx < m and 0 <= ny < n:
                            self.updateBoard(board, [nx, ny])
            else:
                board[x][y] = str(mine)
        return board
