class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def test(a):
            b = max(a - index, 0)
            res = (a + b) * (a - b + 1) // 2

            b = max(a - (n - 1 - index), 0)
            res += (a + b) * (a - b + 1) // 2
            return res - a

        maxSum -= n
        lo, hi = 0, maxSum
        # largest x to satisfy test(x) <= maxSum
        while lo < hi:
            mi = (hi + lo + 1) // 2
            if test(mi) <= maxSum:
                lo = mi
            else:
                hi = mi - 1
        return lo + 1  # add 1 as we subtract 1 from each index in the beginning
