class Solution:
    def countGoodNumbers(self, n: int) -> int:
        m, mod = n // 2, 10 ** 9 + 7
        if n % 2 == 1:
            return pow(5, m + 1, mod) * pow(4, m, mod) % mod
        else:
            return pow(5, m, mod) * pow(4, m, mod) % mod
