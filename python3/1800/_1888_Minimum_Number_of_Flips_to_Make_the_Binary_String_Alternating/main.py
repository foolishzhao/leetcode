class Solution:
    def minFlips(self, s: str) -> int:
        def minFlip(t):
            res, diff = float('inf'), 0
            for i in range(2 * n):
                diff += s[i] != t[i]
                if i >= n:
                    diff -= s[i - n] != t[i - n]
                    res = min(res, diff)
            return res

        n, s = len(s), s + s
        return min(minFlip('10' * n), minFlip('01' * n))
