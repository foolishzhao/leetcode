class Solution:
    def gcd(self, a: int, b: int) -> int:
        if not a:
            return b
        return self.gcd(b % a, a)

    def numUgly(self, n, a, b, c, ab, ac, bc, abc) -> int:
        return n // a + n // b + n // c - n // ab - n // ac - n // bc + n // abc

    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        ab = a * b // self.gcd(a, b)
        ac = a * c // self.gcd(a, c)
        bc = b * c // self.gcd(b, c)
        abc = ab * c // self.gcd(ab, c)

        left, right = 1, (10 ** 9) << 1
        while left <= right:
            mid = (right - left) // 2 + left
            numUgly = self.numUgly(mid, a, b, c, ab, ac, bc, abc)
            if numUgly >= n:
                if mid == left or self.numUgly(mid - 1, a, b, c, ab, ac, bc, abc) < n:
                    return mid
                right = mid - 1
            else:
                left = mid + 1

        return 0


if __name__ == '__main__':
    Solution().nthUglyNumber(4, 2, 3, 4)
