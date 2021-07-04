from typing import List


class Solution:
    # backward
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res, st = list(), list()
        T = T[::-1]
        for i, t in enumerate(T):
            while st and t >= T[st[-1]]:
                st.pop()
            res.append(i - st[-1] if st else 0)
            st.append(i)
        return res[::-1]

    # forward
    def dailyTemperatures2(self, T: List[int]) -> List[int]:
        n = len(T)
        res, st = [0] * n, list()
        for i, t in enumerate(T):
            while st and t > T[st[-1]]:
                j = st.pop()
                res[j] = i - j
            st.append(i)
        return res
