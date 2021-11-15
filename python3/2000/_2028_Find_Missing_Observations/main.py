from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sumRes = (n + len(rolls)) * mean - sum(rolls)
        if sumRes < n or sumRes > 6 * n:
            return list()

        avg, remain = sumRes // n, sumRes % n
        return [avg] * (n - remain) + [avg + 1] * remain
