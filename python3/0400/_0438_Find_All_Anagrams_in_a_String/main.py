from typing import List
import collections


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = list()
        pCnt = collections.defaultdict(int)
        for c in p:
            pCnt[c] += 1

        sCnt = collections.defaultdict(int)
        sLen, pLen, i, t = len(s), len(p), 0, 0
        for c in s:
            sCnt[c] += 1
            if sCnt[c] <= pCnt[c]:
                t += 1
                if t == pLen:
                    res.append(i)
                    t -= 1
                    sCnt[s[i]] -= 1
                    i += 1
            else:
                while sCnt[c] > pCnt[c]:
                    sCnt[s[i]] -= 1
                    if sCnt[s[i]] < pCnt[s[i]]:
                        t -= 1
                    i += 1

        return res

    def findAnagrams2(self, s: str, p: str) -> List[int]:
        dt = collections.defaultdict(int)
        for c in p:
            dt[c] += 1

        res = list()
        sLen, pLen, i, j = len(s), len(p), 0, 0
        while j < sLen:
            if dt[s[j]] > 0:
                dt[s[j]] -= 1
                j += 1

                if j - i == pLen:
                    res.append(i)
            else:
                dt[s[i]] += 1
                i += 1

        return res
