import collections


class Solution:
    def __init__(self):
        self.minStep = float('inf')

    def findMinStep(self, board: str, hand: str) -> int:
        ball = collections.defaultdict(int)
        for c in hand:
            ball[c] += 1

        self.dfs(board, ball, len(hand))
        return -1 if self.minStep == float('inf') else self.minStep

    def dfs(self, board, ball, ballCnt):
        if not board:
            self.minStep = min(self.minStep, ballCnt - sum(ball.values()))
            return

        b = board + "Z"
        i = 0
        for j, c in enumerate(b):
            if c != b[i]:
                s = b[i:j]
                rCnt = max(0, 3 - len(s))
                if ball[b[i]] >= rCnt:
                    ball[b[i]] -= rCnt
                    self.dfs(board[:i] + board[j:], ball, ballCnt)
                    ball[b[i]] += rCnt
                i = j
