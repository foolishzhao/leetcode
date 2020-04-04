from typing import List


class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        s = sum(A)
        F = sum(i * x for i, x in enumerate(A))
        res, n = F, len(A)

        for i in range(n - 1, 0, -1):
            F += s - n * A[i]
            res = max(res, F)

        return res
