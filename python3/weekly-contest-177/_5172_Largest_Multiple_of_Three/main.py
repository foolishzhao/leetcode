from typing import List


class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        digits.sort()
        q, q2, q3 = [], [], []
        for d in digits:
            if d % 3 == 0:
                q.append(d)
            elif d % 3 == 1:
                q2.append(d)
            else:
                q3.append(d)

        s = sum(digits)
        if s % 3 == 1:
            if q2:
                q2 = q2[1:]
            elif len(q3) >= 2:
                q3 = q3[2:]
            else:
                return ""
        elif s % 3 == 2:
            if q3:
                q3 = q3[1:]
            elif len(q2) >= 2:
                q2 = q2[2:]
            else:
                return ""

        q.extend(q2)
        q.extend(q3)
        q.sort(reverse=True)

        res = "".join([str(x) for x in q])
        return "0" if res.startswith("0") else res
