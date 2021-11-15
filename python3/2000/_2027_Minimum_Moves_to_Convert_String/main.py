class Solution:
    def minimumMoves(self, s: str) -> int:
        res, n, i = 0, len(s), 0
        while i < n:
            if s[i] == 'X':
                res += 1
                i += 2
            i += 1
        return res
