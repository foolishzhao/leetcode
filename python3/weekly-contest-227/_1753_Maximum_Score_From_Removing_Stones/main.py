class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        a, b, c = sorted([a, b, c])
        if not a and not b:
            return 0
        elif not a:
            return self.maximumScore(a, b - 1, c - 1) + 1
        else:
            return self.maximumScore(a - 1, b, c - 1) + 1
