from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if not s:
            return []

        res = []
        n, dt = len(s), dict()
        for i in range(n - 9):
            cur = s[i:i + 10]
            dt[cur] = dt.get(cur, 0) + 1
            if dt[cur] == 2:
                res.append(cur)

        return res

    def findRepeatedDnaSequences2(self, s: str) -> List[str]:
        if not s or len(s) <= 10:
            return []

        mask = 0
        for _ in range(10):
            mask <<= 2
            mask |= 3

        res = []
        dt, v = dict(), 0
        for i in range(len(s)):
            v <<= 2
            if s[i] == 'A':
                v |= 0
            elif s[i] == 'C':
                v |= 1
            elif s[i] == 'G':
                v |= 2
            else:
                v |= 3

            v &= mask
            if i >= 9:
                dt[v] = dt.get(v, 0) + 1
                if dt[v] == 2:
                    res.append(s[i - 9:i + 1])

        return res
