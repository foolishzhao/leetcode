class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        return a if a <= 0x7fffffff else ~(a ^ mask)


if __name__ == '__main__':
    Solution().getSum(-1, 1)
