from typing import List


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        res, n, i = 0, len(A), 0
        while i < n:
            j = i + 2
            while j < n and A[j] - A[j - 1] == A[i + 1] - A[i]:
                j += 1

            if j - i >= 3:
                res += (j - i - 2) * (j - i - 1) // 2

            i = j - 1

        return res
