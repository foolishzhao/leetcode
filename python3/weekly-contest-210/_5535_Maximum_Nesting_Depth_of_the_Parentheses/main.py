class Solution:
    def maxDepth(self, s: str) -> int:
        res, d = 0, 0
        for c in s:
            if c == '(':
                d += 1
            if c == ')':
                d -= 1
            res = max(res, d)
        return res
