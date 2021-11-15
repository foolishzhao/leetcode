from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        left, right = [0] * n, [0] * n

        left[0] = grid[0][0]
        for i in range(1, n):
            left[i] += left[i - 1] + grid[0][i]

        right[n - 1] = grid[1][n - 1]
        for i in range(n - 2, -1, -1):
            right[i] += right[i + 1] + grid[1][i]

        return min(max(left[-1] - left[i], right[0] - right[i]) for i in range(n))

    def gridGame2(self, grid: List[List[int]]) -> int:
        score, left, right = float('inf'), sum(grid[0]), 0
        for x, y in zip(grid[0], grid[1]):
            left -= x
            score = min(score, max(left, right))
            right += y
        return score
