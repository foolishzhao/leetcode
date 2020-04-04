class Solution:
    # mutual recursion
    def lastRemaining(self, n: int) -> int:
        return self.leftToRight(n)

    def leftToRight(self, n):
        if n == 1:
            return 1

        return 2 * self.rightToLeft(n // 2)

    def rightToLeft(self, n):
        if n == 1:
            return 1

        if n % 2 == 0:
            return 2 * self.leftToRight(n // 2) - 1
        else:
            return 2 * self.leftToRight(n // 2)

    def lastRemaining2(self, n: int) -> int:
        head, step, remain, left = 1, 1, n, True
        while remain > 1:
            if left or remain % 2 == 1:
                head += step

            remain >>= 1
            step <<= 1
            left = not left

        return head
