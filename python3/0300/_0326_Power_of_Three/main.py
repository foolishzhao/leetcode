class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and not (3 ** 19 % n)
