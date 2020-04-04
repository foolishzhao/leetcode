from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st, dt = list(), dict()
        for x in nums2:
            while st and st[-1] < x:
                dt[st.pop()] = x
            st.append(x)

        return [dt.get(x, -1) for x in nums1]
