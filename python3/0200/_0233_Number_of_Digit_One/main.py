class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0

        res, low, high, bit = 0, 0, n, 0
        while high:
            cur = high % 10
            high //= 10
            if cur == 0:
                res += high * (10 ** bit)
            elif cur == 1:
                res += high * (10 ** bit) + low + 1
            else:
                res += (high + 1) * (10 ** bit)

            low += cur * (10 ** bit)
            bit += 1

        return res
