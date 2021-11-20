from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        st, res = list(), [-1] * len(nums)
        for i, v in enumerate(nums + nums):
            while st and nums[st[-1]] < v:
                res[st.pop()] = v
            if i < len(nums):
                st.append(i)
        return res