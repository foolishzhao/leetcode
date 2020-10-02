import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        upper = int(math.sqrt(c))
        for i in range(upper + 1):
            r = c - i * i
            if int(math.sqrt(r)) ** 2 == r:
                return True
        return False

    def judgeSquareSum2(self, c: int) -> bool:
        lo, hi = 0, int(math.sqrt(c))
        while lo <= hi:
            s = lo ** 2 + hi ** 2
            if s == c:
                return True
            elif s > c:
                hi -= 1
            else:
                lo += 1
        return False
