class Solution:
    def sumBase(self, n: int, k: int) -> int:
        res = 0
        while n:
            x = n % k
            res += x
            n //= k
        return res
