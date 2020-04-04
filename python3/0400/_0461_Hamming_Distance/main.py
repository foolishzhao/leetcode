class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x ^= y
        res = 0
        while x:
            res += 1
            x = x & (x - 1)

        return res
