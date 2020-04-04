import collections
import bisect


class Solution:
    # O(len(t))
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        i, j = 0, 0
        while i < len(t):
            if t[i] == s[j]:
                j += 1
                if j == len(s):
                    return True
            i += 1

        return False

    def isSubsequence2(self, s: str, t: str) -> bool:
        # O(len(t))
        sIdx = collections.defaultdict(list)
        for i, c in enumerate(t):
            sIdx[c].append(i)

        # O(len(s)) * log(len(t))
        prev = 0
        for c in s:
            i = bisect.bisect_left(sIdx[c], prev)
            if i == len(sIdx[c]):
                return False

            prev = sIdx[c][i] + 1

        return True
