from typing import List


class Solution:
    def isSelfCrossing(self, x: List[int]) -> bool:
        i, n = 3, len(x)
        if n < 4:
            return False

        while i < n:
            if x[i] >= x[i - 2] and x[i - 1] <= x[i - 3]:
                return True

            if i >= 4 and x[i - 1] == x[i - 3] and x[i - 4] + x[i] >= x[i - 2]:
                return True

            if i >= 5 and x[i - 1] < x[i - 3] <= x[i - 1] + x[i - 5] and x[i - 4] < x[i - 2] <= x[i] + x[i - 4]:
                return True

            i += 1

        return False
