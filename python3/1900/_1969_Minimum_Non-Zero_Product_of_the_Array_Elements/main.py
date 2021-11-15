class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        if p == 1:
            return 1
        return (2 ** p - 1) * pow(2 ** p - 2, 2 ** (p - 1) - 1, 10 ** 9 + 7) % (10 ** 9 + 7)
