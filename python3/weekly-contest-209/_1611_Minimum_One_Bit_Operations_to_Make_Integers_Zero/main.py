class Solution:
    # https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/discuss/877741/C%2B%2B-solution-with-explanation
    def minimumOneBitOperations(self, n: int) -> int:
        if n <= 1:
            return n

        bit = 0
        while n >= (1 << bit):
            bit += 1

        return ((1 << bit) - 1) - self.minimumOneBitOperations(n - (1 << (bit - 1)))
