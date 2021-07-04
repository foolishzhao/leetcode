from typing import List


class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        for i in range(n):
            for j in range(n):
                if board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j]:
                    return -1

        rowSum, colSum, rowSwap, colSwap = 0, 0, 0, 0
        for i in range(n):
            rowSum += board[0][i]
            colSum += board[i][0]
            rowSwap += board[i][0] == (i % 2)
            colSwap += board[0][i] == (i % 2)

        if rowSum not in [n // 2, (n + 1) // 2]:
            return -1

        if colSum not in [n // 2, (n + 1) // 2]:
            return -1

        if n % 2:
            if rowSwap % 2:
                rowSwap = n - rowSwap

            if colSwap % 2:
                colSwap = n - colSwap
        else:
            rowSwap = min(rowSwap, n - rowSwap)
            colSwap = min(colSwap, n - colSwap)
        return (rowSwap + colSwap) // 2
