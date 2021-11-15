from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        res, st = [0] * n, list()
        for i, t in enumerate(T):
            while st and T[st[-1]] < t:
                j = st.pop()
                res[j] = i - j
            st.append(i)
        return res
