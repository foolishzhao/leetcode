import collections


class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        def isSubseq(substr):
            i = 0
            for j, c in enumerate(s):
                if c == substr[i]:
                    i += 1
                    if i == len(substr):
                        return True
            return False

        counter, q, res = collections.Counter(s), [""], ""
        while q:
            cur = q.pop(0)
            for i in range(26):
                c = chr(ord('a') + i)
                if counter[c] >= k and isSubseq((cur + c) * k):
                    q.append(cur + c)
                    res = cur + c
        return res
