from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return list()

        mIdx = nums.index(max(nums))
        n = len(nums)
        res = [-1] * n
        st = list()
        for i, num in enumerate(nums[mIdx + 1:] + nums[:mIdx + 1]):
            while st and st[-1][1] < num:
                res[st.pop()[0]] = num
            st.append((i, num))

        return res[-mIdx - 1:] + res[:-mIdx - 1]

    def nextGreaterElements2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        st = list()
        for i, num in enumerate(nums + nums):
            while st and nums[st[-1]] < num:
                res[st.pop()] = num
            if i < n:
                st.append(i)
        return res
