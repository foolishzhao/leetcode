class Solution:
    def minOperations(self, n: int) -> int:
        cur = 0
        for i in range(n):
            cur += abs(2 * i + 1 - n)
        return cur // 2
