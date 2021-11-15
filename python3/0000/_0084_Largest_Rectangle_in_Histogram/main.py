from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st, res = [], 0
        for i, h in enumerate(heights + [0]):
            while st and h < heights[st[-1]]:
                j = st.pop()
                res = max(res, heights[j] * (i - st[-1] - 1 if st else i))
            st.append(i)
        return res
