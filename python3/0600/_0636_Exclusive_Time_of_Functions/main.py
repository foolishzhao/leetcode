from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        st, prev = list(), 0
        for log in logs:
            fn, typ, cur = log.split(":")
            fn, cur = int(fn), int(cur)

            if typ == "start":
                if st:
                    res[st[-1]] += cur - prev
                prev = cur
                st.append(fn)
            else:
                res[st[-1]] += cur + 1 - prev
                st.pop()
                prev = cur + 1

        return res
