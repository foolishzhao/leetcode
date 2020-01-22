from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = 0
        st = set(nums)
        for v in nums:
            if v in st:
                st.remove(v)

                left, right = v - 1, v + 1
                while left in st:
                    st.remove(left)
                    left -= 1
                while right in st:
                    st.remove(right)
                    right += 1

                res = max(res, right - left - 1)

        return res
