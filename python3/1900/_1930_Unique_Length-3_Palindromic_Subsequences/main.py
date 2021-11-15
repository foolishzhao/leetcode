import collections
import bisect


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        dt, res = collections.defaultdict(list), 0
        for i, c in enumerate(s):
            dt[ord(c) - ord('a')].append(i)

        for i in range(26):
            if len(dt[i]) <= 1:
                continue

            for j in range(26):
                if i == j:
                    res += len(dt[i]) > 2
                elif len(dt[j]):
                    idx = bisect.bisect_left(dt[j], dt[i][0])
                    res += idx != len(dt[j]) and dt[j][idx] < dt[i][-1]
        return res

    def countPalindromicSubsequence2(self, s: str) -> int:
        res = 0
        for i in range(26):
            c = chr(ord('a') + i)
            i, j = s.find(c), s.rfind(c)
            if i > -1:
                res += len(set(s[i + 1:j]))
        return res
