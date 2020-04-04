from typing import List
import math


class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        res = [1, num + 1]
        t = int(math.sqrt(num + 2))
        for i in range(2, t + 1):
            if (num + 1) % i == 0:
                j = (num + 1) // i
                if j - i <= res[1] - res[0]:
                    res = [i, j]

            if (num + 2) % i == 0:
                j = (num + 2) // i
                if j - i <= res[1] - res[0]:
                    res = [i, j]

        return res
