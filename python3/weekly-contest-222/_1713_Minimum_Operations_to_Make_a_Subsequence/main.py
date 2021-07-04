from typing import List
import bisect


class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        dt = {x: i for i, x in enumerate(target)}
        st = list()
        for a in arr:
            if a not in dt:
                continue

            i = bisect.bisect_left(st, dt[a])
            if i == len(st):
                st.append(dt[a])
            st[i] = dt[a]
        return len(target) - len(st)
