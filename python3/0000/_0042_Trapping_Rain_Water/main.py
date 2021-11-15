from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n, res = len(height), 0
        right = [0] * n
        for i in range(n - 2, -1, -1):
            right[i] = max(height[i + 1], right[i + 1])

        left = 0
        for i in range(n):
            res += max(min(left, right[i]) - height[i], 0)
            left = max(left, height[i])
        return res

    def trap2(self, height: List[int]) -> int:
        left, right, res = height[0], height[-1], 0
        i, j = 1, len(height) - 1
        while i <= j:
            if left <= right:
                res += max(left - height[i], 0)
                left = max(left, height[i])
                i += 1
            else:
                res += max(right - height[j], 0)
                right = max(right, height[j])
                j -= 1
        return res
