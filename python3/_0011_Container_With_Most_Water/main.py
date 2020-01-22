from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        res, n = 0, len(height)
        if n > 1:
            left, right = 0, n - 1
            while left < right:
                res = max(res, (right - left) * min(height[left], height[right]))
                if height[left] <= height[right]:
                    left += 1
                else:
                    right -= 1

        return res
