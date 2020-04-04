from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0

        n = len(triangle)
        for i in range(1, n):
            triangle[i][0] += triangle[i - 1][0]
            for j in range(1, i):
                triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])
            triangle[i][i] += triangle[i - 1][i - 1]

        return min(triangle[n - 1])
