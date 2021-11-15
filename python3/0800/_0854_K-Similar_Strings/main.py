class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        def getNext(s):
            res = list()

            s, i = list(s), 0
            while s[i] == s2[i]:
                i += 1

            for j in range(i + 1, len(s2)):
                if s[j] != s2[j] and s[j] == s2[i]:
                    s[i], s[j] = s[j], s[i]
                    res.append(''.join(s))
                    s[i], s[j] = s[j], s[i]
            return res

        res, q = 0, [s1]
        seen = {s1}
        while q:
            for _ in range(len(q)):
                s = q.pop(0)
                if s == s2:
                    return res

                for ns in getNext(s):
                    if ns not in seen:
                        seen.add(ns)
                        q.append(ns)
            res += 1
