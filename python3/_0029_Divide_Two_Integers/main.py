class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1 if not ((dividend ^ divisor) >> 31) else -1
        dividend, divisor = abs(dividend), abs(divisor)

        res = 0
        while dividend >= divisor:
            shift = 1
            while dividend >= (divisor << shift):
                shift += 1

            res += 1 << (shift - 1)
            dividend -= divisor << (shift - 1)

        res *= sign
        return min(res, (1 << 31) - 1)


if __name__ == '__main__':
    Solution().divide(1, 1)
