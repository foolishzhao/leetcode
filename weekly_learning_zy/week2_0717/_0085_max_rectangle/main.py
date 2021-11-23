from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        ans = 0
        for i, h in enumerate(heights + [0]):
            while stack and h < heights[stack[-1]]:
                p = heights[stack.pop()]
                tmp = p * (i - stack[-1] - 1 if stack else i)
                ans = max(ans, tmp)
            stack.append(i)
        return ans

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        height = [0] * len(len(matrix[0]))
        for i in range (len(matrix)):
            for j in range (len(matrix[0])):
                if matrix[i][j] == '0':
                    height[j] = 0
                else:
                    height[j] += 1
        ans = self.largestRectangleArea(height)
        return ans
