class Solution:
    def reverse(self, x: int) -> int:
        sign, res = 1, 0
        if x < 0:
            sign = -1
            x = -x

        while x:
            res = res * 10 + x % 10
            x //= 10

            if sign * res < -(1 << 31) or sign * res >= (1 << 31):
                return 0

        return sign * res


if __name__ == '__main__':
    Solution().reverse(-123)
