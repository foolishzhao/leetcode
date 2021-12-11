from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        st = []
        for i, v in enumerate(temperatures):
            while st and temperatures[st[-1]] < v:
                cur = st.pop()
                res[cur] = i - cur
            st.append(i)
        return res

