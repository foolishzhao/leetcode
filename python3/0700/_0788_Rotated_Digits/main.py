class Solution:
    def rotatedDigits(self, n: int) -> int:
        def isGood(x):
            good = False
            while x > 0:
                d = x % 10
                if d not in (0, 1, 2, 5, 6, 8, 9):
                    return False

                if d in (2, 5, 6, 9):
                    good = True

                x //= 10
            return good

        return sum([isGood(x) for x in range(1, n + 1)])
