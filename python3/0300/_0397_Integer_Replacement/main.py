class Solution:
    def __init__(self):
        self.memo = dict()

    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0

        if n in self.memo:
            return self.memo[n]

        res = 1
        if n % 2 == 0:
            res += self.integerReplacement(n >> 1)
        else:
            res += min(self.integerReplacement(n - 1), self.integerReplacement(n + 1))

        self.memo[n] = res
        return res
