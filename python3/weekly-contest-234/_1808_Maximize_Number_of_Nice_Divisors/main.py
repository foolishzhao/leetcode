class Solution:
    def maxNiceDivisors(self, n: int) -> int:
        if n < 3:
            return n

        m = 10 ** 9 + 7
        if n % 3 == 0:
            return pow(3, n // 3, m)
        elif n % 3 == 1:
            return pow(3, (n - 4) // 3, m) * 4 % m
        else:
            return pow(3, n // 3, m) * 2 % m
