class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if not n:
            return 0

        left = 31
        while not n & (1 << left):
            left -= 1

        right = left
        while right >= 0 and (m & (1 << right)) == (n & (1 << right)):
            right -= 1

        mask = 0
        for i in range(right + 1, left + 1):
            mask |= 1 << i

        return m & mask

    def rangeBitwiseAnd2(self, m: int, n: int) -> int:
        factor = 1
        while m != n:
            factor <<= 1
            m >>= 1
            n >>= 1

        return m * factor
