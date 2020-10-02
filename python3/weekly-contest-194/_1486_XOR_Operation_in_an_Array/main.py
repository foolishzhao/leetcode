class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = 0
        for i in range(n):
            res ^= (start + 2 * i)
        return res

    # start ^ (start + 2) ^ ... ^ (start + 2 * (n - 1))
    def xorOperation2(self, n: int, start: int) -> int:
        # start ^ (start + 1) ^ ... ^ (start + n - 1)
        # if x is even, x ^ (x + 1) = 1
        def xorA(n, start):
            if start % 2 == 0:
                return xorB(n, start)
            else:
                return (start - 1) ^ xorB(n + 1, start - 1)

        def xorB(n, start):
            if n % 2 == 0:
                return (n // 2) & 1
            else:
                return ((n // 2) & 1) ^ (start + n - 1)

        res = 2 * xorA(n, start // 2)
        if start & n & 1:
            res += 1
        return res
