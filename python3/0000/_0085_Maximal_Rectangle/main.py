from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def maxArea(height):
            res, st = 0, list()
            for i, h in enumerate(height + [0]):
                while st and height[st[-1]] > h:
                    j = st.pop()
                    res = max(res, height[j] * (i - st[-1] - 1 if st else i))
                st.append(i)
            return res

        if not matrix or not matrix[0]:
            return 0

        height, res = [0] * len(matrix[0]), 0
        for row in matrix:
            for j, c in enumerate(row):
                if c == '0':
                    height[j] = 0
                else:
                    height[j] += 1
            res = max(res, maxArea(height))
        return res
