from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board or not board[0]:
            return 0

        res, m, n = 0, len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    if i - 1 >= 0 and board[i - 1][j] == 'X':
                        continue
                    if j - 1 >= 0 and board[i][j - 1] == 'X':
                        continue
                    res += 1

        return res
