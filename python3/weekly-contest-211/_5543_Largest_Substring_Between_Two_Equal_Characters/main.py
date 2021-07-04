import collections


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dt = collections.defaultdict(int)
        res = -1
        for i, c in enumerate(s):
            if c in dt:
                res = max(res, i - dt[c] - 1)
            else:
                dt[c] = i
        return res
