import math


class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9

        upper = 10 ** n - 1
        lower = upper // 10 + 1

        half = (upper ** 2) // (10 ** n)
        while half:
            t = int(str(half) + str(half)[::-1])
            # i >= j, j asc
            for i in range(upper, max(lower - 1, math.floor(math.sqrt(t))), -1):
                if t % i == 0 and lower <= t // i:
                    return t % 1337
            half -= 1

        return 0
