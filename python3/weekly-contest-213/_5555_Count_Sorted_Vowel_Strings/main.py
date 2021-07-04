class Solution:
    def countVowelStrings(self, n: int) -> int:
        a, b, c, d, e = 1, 1, 1, 1, 1
        while n:
            a = a + b + c + d + e
            b = b + c + d + e
            c = c + d + e
            d = d + e
            e = e
            n -= 1
        return a
