class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res = ""
        for i in range(1, n + 1):
            res += bin(i)[2:]
        return int(res, 2) % (10 ** 9 + 7)

    def concatenatedBinary2(self, n: int) -> int:
        res, shift = 0, 0
        for i in range(1, n + 1):
            if i & (i - 1) == 0:
                shift += 1
            res = ((res << shift) | i) % (10 ** 9 + 7)
        return res
