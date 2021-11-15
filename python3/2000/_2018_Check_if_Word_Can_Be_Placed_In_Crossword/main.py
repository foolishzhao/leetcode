from typing import List


class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        def checkHorizon(i, j, word):
            if j > 0 and board[i][j - 1] != '#':
                return False

            if j + len(word) < n and board[i][j + len(word)] != '#':
                return False

            if n - j < len(word):
                return False

            for k, c in enumerate(word):
                if board[i][j + k] == '#':
                    return False

                if board[i][j + k] not in (' ', c):
                    return False

            return True

        def checkVertical(i, j, word):
            if i > 0 and board[i - 1][j] != '#':
                return False

            if i + len(word) < m and board[i + len(word)][j] != '#':
                return False

            if m - i < len(word):
                return False

            for k, c in enumerate(word):
                if board[i + k][j] == '#':
                    return False

                if board[i + k][j] not in (' ', c):
                    return False

            return True

        m, n, rWrod = len(board), len(board[0]), word[::-1]
        return any(checkHorizon(i, j, word) or
                   checkHorizon(i, j, rWrod) or
                   checkVertical(i, j, word) or
                   checkVertical(i, j, rWrod) for i in range(m) for j in range(n))
