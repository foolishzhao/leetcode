from typing import List


class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        n = len(s)
        interval = [[n, 0] for _ in range(26)]
        for i, c in enumerate(s):
            idx = ord(c) - ord('a')
            interval[idx][0] = min(interval[idx][0], i)
            interval[idx][1] = max(interval[idx][1], i)

        def extend(l, r):
            pl, pr = l, r
            for i in range(pl + 1, pr):
                idx = ord(s[i]) - ord('a')
                l = min(l, interval[idx][0])
                r = max(r, interval[idx][1])

            while l != pl or r != pr:
                cl, cr = l, r
                for i in range(cl, pl):
                    idx = ord(s[i]) - ord('a')
                    l = min(l, interval[idx][0])
                    r = max(r, interval[idx][1])
                for i in range(pr + 1, cr):
                    idx = ord(s[i]) - ord('a')
                    l = min(l, interval[idx][0])
                    r = max(r, interval[idx][1])
                pl, pr = cl, cr

            return l, r

        interval = [extend(l, r) for l, r in interval if l <= r]
        interval.sort(key=lambda x: x[1])
        prev, res = -1, list()
        for l, r in interval:
            if l > prev:
                prev = r
                res.append(s[l: r + 1])
        return res
