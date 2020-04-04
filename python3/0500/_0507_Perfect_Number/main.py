import math


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 0:
            return False

        s = 0
        for i in range(1, int(math.sqrt(num)) + 1):
            if num % i == 0:
                j = num // i
                s += i
                if i != j:
                    s += j
        return s == 2 * num
