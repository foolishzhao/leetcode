from typing import List


class Solution:
    def __init__(self):
        def isEnd(board):
            for i in range(3):
                xR, xC, oR, oC = 0, 0, 0, 0
                for j in range(3):
                    xR += board[j][i] == 'X'
                    xC += board[i][j] == 'X'
                    oR += board[j][i] == 'O'
                    oC += board[i][j] == 'O'

                if max(xR, xC, oR, oC) == 3:
                    return True

            xD, xD2, oD, oD2 = 0, 0, 0, 0
            for i in range(3):
                xD += board[i][i] == 'X'
                xD2 += board[i][2 - i] == 'X'
                oD += board[i][i] == 'O'
                oD2 += board[i][2 - i] == 'O'

            return max(xD, xD2, oD, oD2) == 3

        def dfs(board, x):
            t = ''.join(''.join(row) for row in board)
            if t not in self.validSet:
                self.validSet.add(t)
                if not isEnd(board):
                    for i in range(3):
                        for j in range(3):
                            if board[i][j] == ' ':
                                board[i][j] = 'X' if not x else 'O'
                                dfs(board, 1 - x)
                                board[i][j] = ' '

        self.validSet = set()
        dfs([[' '] * 3 for _ in range(3)], 0)

    def validTicTacToe(self, board: List[str]) -> bool:
        return ''.join(board) in self.validSet

    def validTicTacToe2(self, board: List[str]) -> bool:
        def isWin(c):
            for i in range(3):
                if board[i][0] == c and board[i][1] == c and board[i][2] == c:
                    return True

                if board[0][i] == c and board[1][i] == c and board[2][i] == c:
                    return True

            if board[0][0] == c and board[1][1] == c and board[2][2] == c:
                return True

            if board[0][2] == c and board[1][1] == c and board[2][0] == c:
                return True

            return False

        xWin, oWin, turns = isWin('X'), isWin('O'), 0
        for i in range(3):
            for j in range(3):
                turns += board[i][j] == 'X'
                turns -= board[i][j] == 'O'

        return not (turns < 0 or turns > 1 or (turns == 0 and xWin) or (turns == 1 and oWin))
