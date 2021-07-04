class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        # trailing zeros of x!
        def countZero(x):
            res = 0
            while x:
                res += x // 5
                x //= 5
            return res

        # largest number satisfies countZero = t
        def search(t):
            lo, hi = 0, 5 * (k + 1)
            while lo <= hi:
                mi = (hi - lo) // 2 + lo
                cnt = countZero(mi)
                if cnt <= t:
                    lo = mi + 1
                else:
                    hi = mi - 1
            return hi

        return search(k) - search(k - 1)
