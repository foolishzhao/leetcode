from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])

        cur = points[0]
        for i in range(1, m):
            left = [cur[0]] + [0] * (n - 1)
            for j in range(1, n):
                left[j] = max(left[j - 1] - 1, cur[j])

            right = [0] * (n - 1) + [cur[-1]]
            for j in range(n - 2, -1, -1):
                right[j] = max(right[j + 1] - 1, cur[j])

            nxt = [0] * n
            for j in range(n):
                nxt[j] = max(left[j], right[j]) + points[i][j]
            cur = nxt
        return max(cur)
