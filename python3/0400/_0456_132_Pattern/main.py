from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        ak = float('-inf')
        st = list()
        for ai in nums[::-1]:
            if ai < ak:
                return True

            while st and ai > st[-1]:
                ak = st.pop()

            st.append(ai)

        return False
